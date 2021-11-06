# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.home.urls', namespace='home')),
    path('admin/', admin.site.urls),
]
