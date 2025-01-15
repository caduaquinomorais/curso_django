from django.contrib import admin
from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.blog),
    path('exemplo/',blog_views.exemplo),
]
