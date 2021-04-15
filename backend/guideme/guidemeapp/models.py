from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.dispatch import receiver
import os

class Type(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, default='mdi-border-none-variant')

class Activity(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/activities')
    latitude = models.DecimalField(max_digits=7, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    website = models.CharField(max_length=200, null=True)
    types = models.ManyToManyField(Type)

class Rating(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateField(auto_now=True)
    activity = models.ForeignKey(Activity, related_name='ratings', on_delete=models.CASCADE, default=None)
    note = models.IntegerField()
    comment = models.TextField()

@receiver(models.signals.post_delete, sender= Activity)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)