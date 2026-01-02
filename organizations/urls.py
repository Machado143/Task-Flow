# filepath: c:\Codigo\taskflow\organizations\urls.py
from django.urls import path
from django.http import JsonResponse

def example_view(request):
    return JsonResponse({"message": "Organizations API"})

urlpatterns = [
    path('example/', example_view, name='organizations-example'),
]