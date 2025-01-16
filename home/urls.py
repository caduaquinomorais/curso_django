from django.contrib import admin
from django.urls import path
from . import views as home_views


#Seria uma espécie de controller

urlpatterns = [
    path('', home_views.home,name='home'),
]
