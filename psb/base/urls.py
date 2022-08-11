from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name="home"),
   path('trial1/',views.trail1, name="trail1"),
   path('trial2/',views.trail2, name="trail2"),
   path('trial3/',views.trail3, name="trail3"),
   path('trial4/',views.trail4, name="trail4"),
   path('trial5/',views.trail5, name="trail5"),
   path('trial6/',views.trail6, name="trail6"),
   path('trial7/',views.trail7, name="trail7"),
   
]