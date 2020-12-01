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
def Game(request):
    """
        Mini game
        Redirect to login if not already logged (and back to game)
    """

    # get user name    
    UserName = request.user.first_name

    # get plant with pk = question_id or raise 404 error if none
    Vegs = Vegetal.objects.all()
    CurrentPlant = random.choice(Vegetal.objects.all())
    Colors = Color.objects.all()

    Message = f"OK {UserName}, voici la question : \nCite au moins une couleur dominante dans cette plante."

    return render(
        request,
        "knowledge/game.html",
        {
            "Message" : Message,
            "Plant" : CurrentPlant,
            "Colors" : Colors
        })

    # # question with pk = question_id or raise 404 error if none
    # question = get_object_or_404(Question, pk=question_id)

    # try:

    #     # get selected choice (vote)
    #     selected_choice = question.choice_set.get(
    #         pk=request.POST["choice"])

    # except (KeyError, Choice.DoesNotExist):

    #     # in case of error (no choice selected in form)
    #     # redisplay the question voting form with error message
    #     return render(
    #         request, 
    #         'polls/detail.html', 
    #         {
    #             'question': question,
    #             'error_message': "Vous devez choisir une réponse.",
    #         })

    # else:

    #     # if vote is valid, update data in model and commit to DB
    #     selected_choice.votes += 1
    #     selected_choice.save()

    #     # always return an HttpResponseRedirect after successfully dealing with POST data
    #     # prevents data from being posted twice if user hits the Back button
    #     # reverse creates the url to redirect (ie /polls/<question_id>/results)
    #     return HttpResponseRedirect(
    #         reverse(
    #             'polls:results', 
    #             args=(question.id,)
    #             )
    #         )
