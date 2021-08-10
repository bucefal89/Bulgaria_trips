from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Source(models.Model):
    name = models.CharField(
        max_length=50,
    )
    url = models.URLField()

    def __str__(self):
        return f"{self.url}, {self.name}"


class Mountain(models.Model):
    TYPE_CHOICE_MOUNTAIN = 'Berge'
    TYPE_CHOICE_BEACHES = 'Strände'

    TYPE_CHOICES = (
        (TYPE_CHOICE_MOUNTAIN, 'Berg'),
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
        upload_to='photos',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    source = models.ForeignKey(Source, on_delete=models.CASCADE)







