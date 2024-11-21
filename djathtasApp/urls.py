from . import views
from django.urls import path
from .models import *

urlpatterns = [
    path("",views.home,name="home"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("video/",views.video,name="video"),
]