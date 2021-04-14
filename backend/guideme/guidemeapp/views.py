from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from guidemeapp.serializers import UserSerializer, ActivitySerializer, TypeSerializer, RatingSerializer
from guidemeapp.models import Activity, Type, Rating 
import geopy.distance

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    permission_classes_by_action = {    
        'auth': [permissions.IsAuthenticated],
    }

    @action(detail=False, methods=['get'])
    def auth(self, request):
        user = request.user
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]
    permission_classes_by_action = {    
        'area': [permissions.AllowAny],
        'ratings': [permissions.AllowAny],
    }

    @action(detail=False, methods=['post'])
    def area(self, request):
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        radius = request.data['radius']

        pose = (latitude, longitude)
        activities = Activity.objects.all()
        near = []
        for activity in activities:
            activity_pos = (activity.latitude, activity.longitude)
            if geopy.distance.vincenty(pose, activity_pos).km <= radius:
                near.append(activity)

        serializer = ActivitySerializer(near, context={'request': request}, many=True)

        return Response({
            'activities': serializer.data,
        })

    @action(detail=False, methods=['post'])
    def ratings(self, request):
        id = request.data['id']
        activity = Activity.objects.get(pk=id)
        ratings = Rating.objects.filter(activity=activity)
        serializer = RatingSerializer(ratings, context={'request': request}, many=True)
        return Response(serializer.data)


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.AllowAny]

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.AllowAny]