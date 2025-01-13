from . import views
from django.urls import path
from .models import *

urlpatterns = [
    path("",views.home,name="home"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("video/",views.video,name="video"),
    path("anetarsimi/",views.anetarsimi,name="anetarsimi"),
    path('thank-you/', views.thank_you, name="thank_you"), 
    path('artikujt-infomues/', views.artikujinfomues, name='artikujtinfomues'),
    path('artikull/<int:pk>/', views.artikujtinfomues_detail, name='artikujtinfomues_detail'),
    path("votat-e-diaspores/",views.votatediaspores,name="votatediaspores"),
]