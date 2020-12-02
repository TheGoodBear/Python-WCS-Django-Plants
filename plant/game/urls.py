# imports
from django.urls import path

# models imports
from . import views

# namespace
app_name = "game"

# route
urlpatterns = [
    path("", views.Game, name="game"),
    path("<int:plant_id>/", views.Game, name="game"),
]
