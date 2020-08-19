from django.urls import path
from .views import *
from tendencia import views

urlpatterns = [
    path('', views.home),
]
