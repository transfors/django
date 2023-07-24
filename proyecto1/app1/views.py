from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
   		return render(request, 'index.html')

def contador(request):
	texto = request.POST['texto']
	cantidadPalabras = len(texto.split())
	return render(request, 'contador.html', {'cantidad':cantidadPalabras})

