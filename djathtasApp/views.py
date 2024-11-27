from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {}
    return render(request,"home.html",context)


def aboutus(request):
    context={}
    return render(request,"aboutus.html",context)


def video(request):
    video_upload = Video.objects.all()
    context = {"video_upload": video_upload}
    return render(request, "video.html", context)

def anetarsimi(request):
    if request.method == 'POST':
        Anetarsimi.objects.create(
            emer=request.POST.get('emer'),
            mbiemer=request.POST.get('mbiemer'),
            atesi=request.POST.get('atesi'),
            mamesi=request.POST.get('mamesi'),
            vendlindja=request.POST.get('vendlindja'),
            datelindja=request.POST.get('datelindja'),
            nid=request.POST.get('nid'),
            gjinia=request.POST.get('gjinia'),
            arsimi=request.POST.get('arsimi'),
            punesimi=request.POST.get('punesimi'),
            numer_telefoni=request.POST.get('numer-telefoni'),
            email=request.POST.get('email'),
            facebook=request.POST.get('facebook'),
            instagram=request.POST.get('instagram'),
            x=request.POST.get('x'),
            youtube=request.POST.get('youtube'),
            qarku=request.POST.get('qarku'),
            bashkia=request.POST.get('bashkia'),
            emer_mbiemer=request.POST.get('emer-mbiemer'),
            date=request.POST.get('date')
        )
        return HttpResponse("Formulari u dërgua me sukses!")
    context = {}
    return render(request,"anetarsimi.html",context)

