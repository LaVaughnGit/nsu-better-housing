from django.urls import path
from . import views

urlpatterns = [
    path('', views.makoFS, name="makoFS"),
    path('', views.commonsFS, name="commonsFS"),
    path('', views.leogoodwinFS, name="leogoodwinFS"),
    path('', views.clcFS, name="clcFS"),
    path('', views.vettelFS, name="vettelFS"),
    path('', views.farquharFS, name="farquharFS"),
    path('', views.foundersFS, name="foundersFS"),
    path('', views.rollingFS, name="rollingFS"),
]
