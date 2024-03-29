from django.urls import path
from . import views
urlpatterns = [

    path('cse', views.cse, name="cse"),
    path('ise', views.ise, name="ise"),
    path('ece', views.ece, name="ece"),
    path('civil', views.civil, name="civil"),
    
]