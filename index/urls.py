from django.urls import path
from . import views
urlpatterns = [

    path('Index', views.Index , name="Index"),
    path('Votingpage', views.Votingpage , name="Votingpage"),
  
]