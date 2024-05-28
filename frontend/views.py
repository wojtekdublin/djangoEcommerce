from django.shortcuts import render
from .models import Item

# Create your views here.

def home(request):

    context = {
        'items': Item.objects.all()
    }

    return render (request, 'home.html', context) 