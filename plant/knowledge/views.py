from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Vegetal, Category


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

        # a=""
        # for veg in VegetalList:
        #     a += f"{veg.name}"

        return VegetalList



class DetailView(generic.DetailView):
    """
    """

    model = Vegetal
    template_name = "knowledge/detail.html"


    # def get_queryset(self):
    #     """
    #         Excludes any questions that aren't published yet.
    #     """
    #     return Question.objects.filter(pub_date__lte=timezone.now())


# non generic views
# -----------------

def Game(request, question_number=None):
    """
    """
    
    Message = "Pas de question"
    if question_number is not None:
        Message = f"Question {question_number}"

    return render(
        request,
        "knowledge/game.html",
        {"Message" : Message})

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
