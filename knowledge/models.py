from django import forms
from django.db import models
from django.db.models.fields import Field
from django.contrib.auth.models import User

# Models

class Category(models.Model):
    """
    """

    name = models.CharField(
        "Nom", 
        max_length=50)
    # recursive foreign key
    parent = models.ForeignKey(
        "self", 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        verbose_name="Catégorie parente")


    def __str__(self):
        """
        """

        return f"{self.name}"


    class Meta:
        """
        """

        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ["name"]



class Color(models.Model):
    """
    """

    name = models.CharField(
        "Nom", 
        max_length=30)


    def __str__(self):
        """
        """

        return f"{self.name}"


    class Meta:
        """
        """

        verbose_name = "Couleur"
        verbose_name_plural = "Couleurs"
        ordering = ["name"]



class Vegetal(models.Model):
    """
    """

    name = models.CharField(
        "Nom", 
        max_length=50)
    wiki = models.URLField(
        "URL Wikipedia", 
        max_length=150, 
        blank=True)
    # file upload image file (can be empty)
    image = models.ImageField(
        "Image", 
        upload_to="", 
        blank=True)
    # field displayed with TextArea instead of TextInput
    comments = models.TextField(
        "Commentaires", 
        max_length=1000, 
        blank=True)
    # foreign key to Category model (1 to many)
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT, 
        verbose_name="Catégorie")
    # foreign key to Color model (many to many) - could also be placed in Color
    color = models.ManyToManyField(
        Color, 
        verbose_name="Couleurs dominantes")


    def __str__(self):
        """
        """

        return f"{self.name}"


    class Meta:
        """
        """

        verbose_name = "Plante"
        verbose_name_plural = "Plantes"
        ordering = ["name"]
