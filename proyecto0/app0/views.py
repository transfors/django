from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('<h1><strong>Bienvenidos al Curso De Django</Strong></h1>')
    return render(request, 'index.html') 
