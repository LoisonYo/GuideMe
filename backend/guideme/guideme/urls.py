from django.contrib import admin
from django.urls import include, path
from guidemeapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('api', include('guidemeapp.urls')),
    path('admin', admin.site.urls),
] + static('/images/', document_root='images/')
