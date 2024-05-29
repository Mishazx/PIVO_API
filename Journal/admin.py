from django.contrib import admin

from Journal.models import BrewingEvent


class BrewingEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'production_line', 'event_type', 'event_date', 'description')
    list_display_links = ('id', 'event_type')
    search_fields = ('event_type', 'description')
    
    
admin.site.register(BrewingEvent, BrewingEventAdmin)