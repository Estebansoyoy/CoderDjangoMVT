from multiprocessing import context
from django.shortcuts import render
from Tienda.models import Distribuidor


# Create your views here.
def hola(request):
    return render(request, "miarchivo.html", context={})

def verDistribuidor(request):
    distribuidor = Distribuidor.objects.all()
    return render(request, "distribuidor.html", context={'lista': distribuidor})


