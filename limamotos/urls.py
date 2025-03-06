from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Site rodando corretamente!")

urlpatterns = [
    path('', home),
]
