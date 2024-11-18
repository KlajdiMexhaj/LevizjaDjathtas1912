from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request,"home.html",context)


def aboutus(request):
    context={}
    return render(request,"aboutus.html",context)
