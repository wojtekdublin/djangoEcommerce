from django.shortcuts import render
from .models import Item
from django.views.generic import View, DetailView, ListView

# Create your views here.

#def home(request):
#
#    context = {
#        'items': Item.objects.all()
#    }
#    return render (request, 'home.html', context) 

class HomeView(ListView):
    model = Item
    paginate_by = 6
    template_name = 'home.html'

class ProductDetailView(DetailView):
    model = Item
    template_name = 'detail.html'
