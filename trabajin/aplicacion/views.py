from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'aplicacion/home.html')

def about(request):
    return render(request, 'aplicacion/about.html')