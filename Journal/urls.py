from django.urls import path
from . import views

urlpatterns = [
    path('get_brewing_events/', views.get_brewing_events),
]