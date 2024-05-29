from django.contrib import admin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'production_line', 'photo']
    search_fields = ['full_name']

admin.site.register(Employee, EmployeeAdmin)