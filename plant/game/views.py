import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from knowledge.models import Vegetal, Category, Color


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

    # get current user
    CurrentUser = request.user

    # get plant (random choice or by plant_id)
    CurrentPlant = random.choice(Vegetal.objects.all())
    if plant_id:
        CurrentPlant = get_object_or_404(
            Vegetal, 
            pk=plant_id)
    
    # get all existing colors
    Colors = Color.objects.all()

    # Define default message
    Message = f"OK {CurrentUser.first_name}, voici la question : \nDans la liste ci-dessous, sélectionne une couleur dominante de cette plante."

    # if action is post (plant_id is passed in parameters)
    if plant_id:
        # get post result for Color input (radio button) or none if no button was selected
        SelectedColorID = request.POST.get("Color", None)
        if SelectedColorID is None:
            # no button was selected
            Message = f"{CurrentUser.first_name}, tu dois sélectionner une couleur dans la liste."
        else:
            # a button was selected
            try:
                # get plant color matching selected answer
                PlantColor = CurrentPlant.color.get(
                    pk=SelectedColorID)
                # success
                # update user data
                CurrentUser.userdata.good_answers += 1
                CurrentUser.userdata.save()
                # define message
                Message = f"BRAVO {CurrentUser.first_name},\n{PlantColor.name} est bien une couleur dominante de {CurrentPlant.name} !\n\nCette bonne réponse est ajoutée à ton profil."
                # reset Colors so form won't be displayed anymore in view
                Colors = None
            except (KeyError, Color.DoesNotExist):
                # error, this plant don't have this color
                # get color object
                SelectedColor = Color.objects.get(
                    pk=SelectedColorID)
                # update user data
                CurrentUser.userdata.bad_answers += 1
                CurrentUser.userdata.save()
                # define message
                Message = f"Désolé {CurrentUser.first_name},\n{SelectedColor.name} n'est pas une couleur dominante de {CurrentPlant.name}.\nLes bonnes réponses sont {', '.join(Color.name for Color in CurrentPlant.color.all())}\n\nMalheureusement, cette mauvaise réponse est ajoutée à ton profil."
                # reset Colors so form won't be displayed anymore in view
                Colors = None

    # render template with appropriate context :
    #   - Message to show to user
    #   - Current plant object
    #   - List of colors to create form with radio buttons
    #       (None if answer was found -> no form will be created)
    return render(
        request,
        f"game/game.html",
        {
            "Message" : Message,
            "Plant" : CurrentPlant,
            "Colors" : Colors
        })
