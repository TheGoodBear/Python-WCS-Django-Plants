from django import forms
from django.db import models
from django.db.models.fields import Field

# Models

class Category(models.Model):
    """
    """

    name = models.CharField("Nom", max_length=50)
    # recursive foreign key
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        """
        """

        return f"{self.name}"



class Color(models.Model):
    """
    """

    name = models.CharField("Nom", max_length=30)


    def __str__(self):
        """
        """

        return f"{self.name}"



class Vegetal(models.Model):
    """
    """

    name = models.CharField("Nom", max_length=50)
    wiki = models.URLField("Wikipedia", max_length=150, blank=True)
    # file upload image file (can be empty)
    image = models.ImageField("Image", upload_to="", blank=True)
    # field displayed with TextArea instead of TextInput
    comments = models.TextField("Commentaires", max_length=1000, blank=True)
    # foreign key to Category model (1 to many)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # foreign key to Color model (many to many) - could also be placed in Color
    color = models.ManyToManyField(Color)


    def __str__(self):
        """
        """

        return f"{self.name}"
