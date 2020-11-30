from django.http import HttpResponse
from django.shortcuts import render


# Views

def index(request):
    return HttpResponse("Salut, bienvenue sur l'application.")
