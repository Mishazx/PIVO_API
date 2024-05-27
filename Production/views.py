from django.shortcuts import render
from django.http import JsonResponse

from Production.utils import get_characteristic_production_lines, get_performance_production_lines, get_storage_data
from.models import BrewingEvent, ProductionLinePerformance


def get_brewing_events(request):
    data = list(BrewingEvent.objects.values('id', 'production_line__name', 'event_type', 'event_date', 'description')[::-1])
    return JsonResponse(data, safe=False)


def get_production(request):
    performance_data = get_performance_production_lines()
    storage_data = get_storage_data()
    characteristic_data = get_characteristic_production_lines()
    
    all_data = {
        'storage': storage_data,
        'performance': performance_data,
        'characteristic': characteristic_data,
    }

    return JsonResponse(all_data, safe=False)