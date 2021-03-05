from django.contrib.auth.models import User, Activity, Type, Rating
from rest_framework import serializers

class UserSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'name', 'email', 'password']

class ActivitySerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Activity
        field = ['url', 'creator', 'name', 'description', 'image', 'longitude', 'latitude']

class TypeSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Type
        field = ['url', 'name']

class RatingSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Rating
        field = ['url', 'note', 'comment']


#a voir avec l'assistant