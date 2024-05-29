from django.shortcuts import render
from django.http import JsonResponse

from Journal.models import BrewingEvent

# Create your views here.
def get_brewing_events(request):
    data = list(BrewingEvent.objects.values('id', 'production_line__name', 'event_type', 'event_date', 'description')[::-1])
    return JsonResponse(data, safe=False)
