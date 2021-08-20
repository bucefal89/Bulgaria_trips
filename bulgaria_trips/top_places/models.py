from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Place(models.Model):
    Name = models.CharField(
        max_length=50,
    )
    Beschreibung = models.CharField(
        max_length=100,
    )
    Bezeichnung = models.TextField(
        max_length=1500,
    )
    Bild = models.ImageField(
        upload_to='photos_places',
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
