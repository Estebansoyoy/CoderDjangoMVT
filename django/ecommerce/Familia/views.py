from django.shortcuts import render
from Familia.models import Familiares
# Create your views here.

def hola(request):
    return render(request, "miarchivo.html", context={})

def verFamilia(request):
    familia = Familiares.objects.all()
    return render(request, "familia.html", context={'lista': familia})