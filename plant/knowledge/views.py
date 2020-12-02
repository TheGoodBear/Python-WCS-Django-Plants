import random

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




# non generic views
# -----------------

@login_required(login_url="/admin/login/?next=/game/")
def Game(request, plant_id=None):
    """
        Mini game
        @ -> Redirect to login if not already logged (and back to game)
        if not plant_id draw random plant from Vegetal collection
        else check for selected answer
    """

    # get user name    
    UserName = request.user.first_name

    # get plant (random choice or by plant_id)
    CurrentPlant = random.choice(Vegetal.objects.all())
    if plant_id:
        CurrentPlant = get_object_or_404(
            Vegetal, 
            pk=plant_id)
    
    # get all existing colors
    Colors = Color.objects.all()

    # Define default message
    Message = f"OK {UserName}, voici la question : \nDans la liste ci-dessous, sélectionne une couleur dominante de cette plante."

    # if action is post (plant_id is passed in parameters)
    if plant_id:
        # get post result for Color input (radio button) or none if no button was selected
        SelectedColorID = request.POST.get("Color", None)
        if SelectedColorID is None:
            # no button was selected
            Message = f"{UserName}, tu dois sélectionner une couleur dans la liste."
        else:
            # a button was selected
            try:
                # get plant color matching selected answer
                PlantColor = CurrentPlant.color.get(
                    pk=SelectedColorID)
                # success
                Message = f"BRAVO {UserName},\n{PlantColor.name} est bien une couleur dominante de {CurrentPlant.name} !"
                Colors = None
            except (KeyError, Color.DoesNotExist):
                # error, this plant don't have this color
                # get color object
                SelectedColor = Color.objects.get(
                    pk=SelectedColorID)
                Message = f"Désolé {UserName},\n{SelectedColor.name} n'est pas une couleur dominante de {CurrentPlant.name}.\nLes bonnes réponses sont {', '.join(Color.name for Color in CurrentPlant.color.all())}"

    # render template with appropriate context :
    #   - Message to show to user
    #   - Current plant object
    #   - List of colors to create form with radio buttons
    #       (None if answer was found -> no form will be created)
    return render(
        request,
        f"knowledge/game.html",
        {
            "Message" : Message,
            "Plant" : CurrentPlant,
            "Colors" : Colors
        })
