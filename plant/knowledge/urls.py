# imports
from django.urls import path


# models imports
from . import views


# namespace
app_name = "knowledge"
# route
urlpatterns = [
    path("", views.index, name="index")     # url = /<app name>/
]
