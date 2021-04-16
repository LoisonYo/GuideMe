from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from guidemeapp.serializers import UserSerializer, ActivitySerializer, TypeSerializer, RatingSerializer
from guidemeapp.models import Activity, Type, Rating
from guidemeapp.permissions import UserPermission, ActivityPermission, TypePermission, RatingPermission
import geopy.distance

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

    @action(detail=False, methods=['get'])
    def auth(self, request):
        user = request.user
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [ActivityPermission]

    @action(detail=False, methods=['post'])
    def area(self, request):
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        radius = int(request.data['radius']) / 1000

        pose = (latitude, longitude)
        activities = Activity.objects.all()
        near = []
        for activity in activities:
            activity_pos = (activity.latitude, activity.longitude)
            if geopy.distance.distance(pose, activity_pos).km <= radius:
                near.append(activity)

        serializer = ActivitySerializer(near, context={'request': request}, many=True)

        return Response({
            'activities': serializer.data,
        })

    @action(detail=False, methods=['get'])
    def user(self, request):
        activities = Activity.objects.filter(creator=request.user)
        serializer = ActivitySerializer(activities, context={'request': request}, many=True)
        return Response({ 'activities': serializer.data })

    @action(detail=False, methods=['get'])
    def ratings(self, request):
        ratings = Rating.objects.filter(activity=request.query_params['id'])
        serializer = RatingSerializer(ratings, context={'request': request}, many=True)
        return Response({ 'ratings': serializer.data })

    @action(detail=False, methods=['get'])
    def types(self, request):
        types = Type.objects.filter(activity=request.query_params['id'])
        serializer = TypeSerializer(types, context={'request': request}, many=True)
        return Response({ 'types': serializer.data })

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [TypePermission]

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [RatingPermission]