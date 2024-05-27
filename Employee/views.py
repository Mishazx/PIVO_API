from django.shortcuts import render
from django.http import JsonResponse

from .models import Employee


def get_employees(request):
    data = list(Employee.objects.values('full_name', 'position', 'photo', 'production_line'))
    return JsonResponse(data, safe=False)
