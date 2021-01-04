import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from knowledge.models import Vegetal, Category, Color
from game.models import UserData


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
    # get friendly user name (first_name if exists, else username)
    CurrentUserName = CurrentUser.first_name if CurrentUser.first_name.strip() else CurrentUser.username

    # check if UserData exists (1 to 1 relation with auth_user)
    try:
        CurrentUserData = CurrentUser.userdata
    except UserData.DoesNotExist:
        CurrentUserData = UserData()
        CurrentUserData.user_id = CurrentUser.id
        CurrentUserData.save()
        print(f"User data created for user ({CurrentUser.id}) - {CurrentUserName}")

    # proceed with game if all is OK
    ProceedWithGame = True
    CurrentPlant = None
    Colors = None
    Message = ""

    # get plant (random choice or by plant_id)
    try:
        CurrentPlant = random.choice(Vegetal.objects.all())
        if plant_id:
            CurrentPlant = get_object_or_404(
                Vegetal, 
                pk=plant_id)
    except IndexError:
        ProceedWithGame = False
        Message = f"Désolé {CurrentUserName}, mais il n'existe aucune plante dans la base.\nIl n'est donc pas possible de jouer pour le moment."

    # start game
    if ProceedWithGame:
        # get all existing colors
        Colors = Color.objects.all()

        # Define default message
        Message = f"OK {CurrentUserName}, voici la question : \nDans la liste ci-dessous, sélectionne une couleur dominante de cette plante."

        # if action is post (plant_id is passed in parameters)
        if plant_id:
            # get post result for Color input (radio button) or none if no button was selected
            SelectedColorID = request.POST.get("Color", None)
            if SelectedColorID is None:
                # no button was selected
                Message = f"{CurrentUserName}, tu dois sélectionner une couleur dans la liste."
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
                    Message = f"BRAVO {CurrentUserName},\n{PlantColor.name} est bien une couleur dominante de {CurrentPlant.name} !\n\nCette bonne réponse est ajoutée à ton profil."
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
                    GoodAnswers = (
                        f"La bonne réponse est : {[Color.name for Color in CurrentPlant.color.all()][0]}."
                        if len(CurrentPlant.color.all()) == 1
                        else f"Les bonnes réponses sont : {', '.join(Color.name for Color in CurrentPlant.color.all())}.")
                    Message = f"Désolé {CurrentUserName},\n{SelectedColor.name} n'est pas une couleur dominante de {CurrentPlant.name}.\n{GoodAnswers}\n\nMalheureusement, cette mauvaise réponse est ajoutée à ton profil."
                    # reset Colors so form won't be displayed anymore in view
                    Colors = None
                
                # update message with score overview
                Message += f"\nTu as donc au total : {CurrentUser.userdata.good_answers} bonnes réponses et {CurrentUser.userdata.bad_answers} mauvaises réponses."

    # render template with appropriate context :
    #   - Message to show to user
    #   - Current plant object
    #   - List of colors to create form with radio buttons
    #       (None if answer was given -> no form will be created)
    return render(
        request,
        f"game/game.html",
        {
            "Message" : Message,
            "Plant" : CurrentPlant,
            "Colors" : Colors
        })
