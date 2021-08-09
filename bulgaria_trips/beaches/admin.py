from django.contrib import admin

from bulgaria_trips.beaches.models import Beach, SourceBeaches


@admin.register(Beach)
class BeachUserAdmin(admin.ModelAdmin):
    pass


@admin.register(SourceBeaches)
class SourceUserAdmin(admin.ModelAdmin):
    pass
