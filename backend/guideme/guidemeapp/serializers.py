from django.contrib.auth.models import User
from guidemeapp.models import Activity, Type, Rating
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name', 'icon']

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects)
    activity = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Activity.objects)
    
    class Meta:
        model = Rating
        fields = ['id', 'note', 'date', 'comment', 'creator', 'activity']

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects)
    types = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Type.objects)
    ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Rating.objects)
    note = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'creator', 'name', 'description', 'longitude', 'latitude', 'website', 'types', 'image', 'ratings', 'note']

    def get_note(self, objects):
        notes = set(map(lambda r: r.note, objects.ratings.all()))
        if len(notes) > 0:
            note = sum(notes) / len(notes)
            return format(note, '.1f')
        else:
            return 5
