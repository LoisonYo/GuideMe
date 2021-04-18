from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.dispatch import receiver
import os

# Type d'une activité
# p.ex. Sport, Equipe, Nourriture, Livraison, etc...
#
# name : Nom (p.ex. Sport)
# icon : Nom de l'icone mdi à utiliser (p.ex. mdi-run)
#
# Relations :
#       Type n <------> n Activity
class Type(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, default='mdi-border-none-variant')

# Activity
#
# name : Nom de l'activité
# description : Description de l'activité
# latitiude : Latitude du lieu de l'activité
# longitude : Longitude du lieu de l'activité
# website : Lien du site internet de l'activité
# image : Image en rapport avec l'activité
#
# Relations :
#       Activity n <------> n Type
#       Activity n <------> 1 User
#       Activity 1 <------> n Rating
class Activity(models.Model):
    types = models.ManyToManyField(Type)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/activities')
    latitude = models.DecimalField(max_digits=7, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    website = models.CharField(max_length=200, null=True)

# Rating
#
# date : Date du commentaire
# comment : Commentaire sur l'activité
# note : Note attribuée à l'activité
#
# Relations :
#       Rating n <------> 1 Activity
#       Rating n <------> 1 User
class Rating(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    activity = models.ForeignKey(Activity, related_name='ratings', on_delete=models.CASCADE, default=None)

    date = models.DateField(auto_now=True)
    note = models.IntegerField()
    comment = models.TextField()

    class Meta:
        unique_together = ('creator', 'activity',)