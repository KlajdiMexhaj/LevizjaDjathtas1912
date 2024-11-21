from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    context = {}
    return render(request,"home.html",context)


def aboutus(request):
    context={}
    return render(request,"aboutus.html",context)


def video(request):
    video_upload = Video.objects.all()
    context={"video_upload":video_upload}
    return render(request,"video.html",context)



