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
]