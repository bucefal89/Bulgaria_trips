from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class SourceBeaches(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Beach(models.Model):
    TYPE_CHOICE_BEACHES = 'Strände'

    TYPE_CHOICES = (
        (TYPE_CHOICE_BEACHES, 'Stränd'),
        # (TYPE_CHOICE_BEACHES, 'Stränd'),
    )

    Typ = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
    )

    Name = models.CharField(
        max_length=150,
    )
    Bezeichnung = models.TextField(
        max_length=500,
    )
    Bild = models.ImageField(
        upload_to='photos_beaches',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    source = models.ForeignKey(SourceBeaches, on_delete=models.CASCADE)