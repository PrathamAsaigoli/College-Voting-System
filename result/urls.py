from django.urls import path
from . import views

urlpatterns = [

    path('csepresidentinput' , views.csepresidentinput, name='csepresidentinput'),
    path('csevicepresidentinput' ,views.csevicepresidentinput , name='csevicepresidentinput' ),
    path('csesecretoryinput',views.csesecretoryinput, name='csesecretoryinput' ),

    path('csepresidentresult' , views.csepresidentresult , name='csepresidentresult'),
]