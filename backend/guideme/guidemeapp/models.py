from django.db import models

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Activities(models.Model):
    creator = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FilePathField(path=images_path)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    latitude = models.DecimalField(max_digits=7, decimal_places=5)

class Ratings(models.Model):
    user_id = models.IntegerField()
    activity_id = models.IntegerField()
    note = models.IntegerField()
    comment = models.TextField()

class Types(models.Model):
    name = models.CharField(max_length=50)

class Types_Activities(models.Model):
    type_id = models.IntegerField()
    activity_id = models.IntegerField()
