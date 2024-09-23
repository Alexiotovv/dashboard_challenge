from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard, name='home'),
    path('mysql', dashboard_mysqlconnector, name='home_mysqlconnector'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
