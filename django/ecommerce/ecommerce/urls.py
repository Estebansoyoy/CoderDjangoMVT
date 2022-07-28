from django.contrib import admin
from django.urls import path
from Tienda.views import hola, verDistribuidor
from Familia.views import verFamilia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('holamundo/',hola),
    path('Distribuidor/',verDistribuidor),
    path('Familia/',verFamilia),
]
