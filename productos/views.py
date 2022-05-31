from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("hola mundo")


def hola_soy_una_plantilla(request):
    return HttpResponse(render(request, 'productos/index.html', {} ))