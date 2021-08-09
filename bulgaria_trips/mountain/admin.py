from django.contrib import admin

from bulgaria_trips.mountain.models import Mountain, Source


@admin.register(Mountain)
class MountainUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Source)
class SourceUserAdmin(admin.ModelAdmin):
    pass
