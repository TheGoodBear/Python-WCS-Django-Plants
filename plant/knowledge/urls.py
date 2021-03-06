# imports
from django.urls import path

# models imports
from . import views

# namespace
app_name = "knowledge"

# route
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("knowledge/", views.IndexView.as_view(), name="index"),    
    path("knowledge/<int:pk>/", views.DetailView.as_view(), name="detail"),
]
