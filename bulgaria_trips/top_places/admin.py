from django.contrib import admin

# Register your models here.
from bulgaria_trips.top_places.models import Place


@admin.register(Place)
class PlaceUserAdmin(admin.ModelAdmin):
    pass
