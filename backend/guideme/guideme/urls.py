from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from guidemeapp import views

urlpatterns = [
    path('', include('guidemeapp.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)