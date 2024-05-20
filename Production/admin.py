from django.contrib import admin

from.models import ProductionLine, BrewingEvent
from.models import Equipment, TechnicalService, ProductionLinePerformance


class ProductionLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    
class BrewingEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'production_line', 'event_type', 'event_date', 'description')
    list_display_links = ('id', 'event_type')
    search_fields = ('event_type', 'description')
    


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ( 'production_line', 'name', 'description')
    search_fields = ('name',)
admin.site.register(Equipment, EquipmentAdmin)


class TechnicalServiceAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'service_date', 'description')
    search_fields = ('equipment__name',)
admin.site.register(TechnicalService, TechnicalServiceAdmin)


class ProductionLinePerformanceAdmin(admin.ModelAdmin):
    list_display = ('production_line', 'timestamp', 'performance')
    list_filter = ('production_line', 'timestamp')
    search_fields = ('production_line__name', 'timestamp')
    # admin.site.register(ProductionLine, ProductionLineAdmin)

admin.site.register(ProductionLinePerformance, ProductionLinePerformanceAdmin)

    
admin.site.register(BrewingEvent, BrewingEventAdmin)
    
admin.site.register(ProductionLine, ProductionLineAdmin)