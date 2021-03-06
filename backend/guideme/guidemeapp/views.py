from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from guidemeapp.serializers import UserSerializer

# Create your views here.
def test(request):
    return HttpResponse("Backend OK")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]