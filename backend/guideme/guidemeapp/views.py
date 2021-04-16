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

# ViewSet du modèle User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

    # Retourne l'utilisateur authentifié'
    #
    # Method : GET
    #
    # Returns : L'utilisateur authentifié
    #
    @action(detail=False, methods=['get'])
    def auth(self, request):
        user = request.user
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

# ViewSet du modèle Activity
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [ActivityPermission]

    # Retourne les activité dans un rayon donné
    #
    # Method : GET
    # Params :
    #       latitude : Latitude du point
    #       longitude : Longitude du point
    #       radius : Rayon de la recherche
    #
    # Returns : Liste des activités dans un rayon donné
    #
    @action(detail=False, methods=['get'])
    def area(self, request):
        latitude = request.query_params['latitude']
        longitude = request.query_params['longitude']
        radius = int(request.query_params['radius']) / 1000

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

    # Retourne les activités créées par l'utilisateur authentifié
    #
    # Method : GET
    #
    # Returns : Liste des activités créées par l'utilisateur authentifié
    #
    @action(detail=False, methods=['get'])
    def user(self, request):
        activities = Activity.objects.filter(creator=request.user)
        serializer = ActivitySerializer(activities, context={'request': request}, many=True)
        return Response({ 'activities': serializer.data })

    # Retourne les commentaires d'une activité donnée
    #
    # Method : GET
    # Params :
    #       id : L'id de l'activité
    #
    # Returns : Liste des commentaires d'une activité donnée
    #
    @action(detail=False, methods=['get'])
    def ratings(self, request):
        ratings = Rating.objects.filter(activity=request.query_params['id'])
        serializer = RatingSerializer(ratings, context={'request': request}, many=True)
        return Response({ 'ratings': serializer.data })

    # Retourne les types d'une activité donnée
    #
    # Method : GET
    # Params :
    #       id : L'id de l'activité
    #
    # Returns : Liste des types d'une activité donnée
    #
    @action(detail=False, methods=['get'])
    def types(self, request):
        types = Type.objects.filter(activity=request.query_params['id'])
        serializer = TypeSerializer(types, context={'request': request}, many=True)
        return Response({ 'types': serializer.data })

# ViewSet du modèle Type
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [TypePermission]

# ViewSet du modèle Rating
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [RatingPermission]