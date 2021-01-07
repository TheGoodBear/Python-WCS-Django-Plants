from django.db import models
from django.contrib.auth.models import User


# Models
class UserData(models.Model):
    """
    """

    # FK to user (auth_user)
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE)
    # additional user data
    good_answers = models.IntegerField(
        "Bonnes réponses", 
        default=0)
    bad_answers = models.IntegerField(
        "Mauvaises réponses", 
        default=0)


    class Meta:
        """
        """

        verbose_name_plural = "Données additionnelles"
