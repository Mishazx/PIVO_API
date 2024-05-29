from django.contrib import admin

# import Employee


from.models import Equipment, TechnicalService, StorageData
from .models import ProductionLine, ProductionLinePerformance, CharacteristicProductionLine


class ProductionLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    
    



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
    
# from django.contrib import admin


class CharacteristicProductionLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'production_line', 'status', 'efficiency', 'operational_hours', 'maintenance_frequency', 'energy_consumption', 'staff_required', 'downtime_per_month')
    list_filter = ('production_line', 'maintenance_frequency')
    search_fields = ('production_line__name', 'maintenance_frequency')
    ordering = ('production_line', 'id')

# Register the admin class with the associated model


    
class StorageDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('count',)
    
    
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'full_name', 'position', 'production_line', 'photo_preview')
#     search_fields = ('full_name', 'position', 'production_line')
#     list_filter = ('position', 'production_line')
    
#     def photo_preview(self, obj):
#         if obj.photo:
#             return '<img src="{}" width="50" height="50" />'.format(obj.photo.url)
#         return '(No photo)'
    
#     photo_preview.allow_tags = True
#     photo_preview.short_description = 'Фото'

# admin.site.register(Employee, EmployeeAdmin)
    
    
admin.site.register(StorageData, StorageDataAdmin)

admin.site.register(ProductionLinePerformance, ProductionLinePerformanceAdmin)
admin.site.register(CharacteristicProductionLine, CharacteristicProductionLineAdmin)
    

    
admin.site.register(ProductionLine, ProductionLineAdmin)