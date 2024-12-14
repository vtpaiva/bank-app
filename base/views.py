from django.shortcuts import render
from .models import Client

# Create your views here.

def home(request):
    clients = Client.objects.all()

    context = {
        'clients': clients
    }

    return render(request, 'home.html', context)