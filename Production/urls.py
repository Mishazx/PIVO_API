from django.urls import path
from . import views

urlpatterns = [
    path('get_production/', views.get_production),
]