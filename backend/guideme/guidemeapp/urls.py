from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'types', views.TypeViewSet)
router.register(r'ratings', views.RatingViewSet)


urlpatterns = [
    path('/', include(router.urls)),
    path('/login/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]