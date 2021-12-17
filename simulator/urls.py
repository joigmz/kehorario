from django.urls import path

from . import views

urlpatterns = [
    path('simulador', views.simulator, name='simulator')
]