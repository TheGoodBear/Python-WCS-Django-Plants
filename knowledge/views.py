from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Vegetal, Category, Color


# Views

# generic

class IndexView(generic.ListView):
    """
    """

    template_name = "knowledge/index.html"
    context_object_name = "latest_plants"


    def get_queryset(self):
        """
            Return the last 10 plants in DB
        """

        VegetalList = (Vegetal.objects
            .order_by("-id")
            [:10])

        return VegetalList



class DetailView(generic.DetailView):
    """
    """

    model = Vegetal
    template_name = "knowledge/detail.html"

