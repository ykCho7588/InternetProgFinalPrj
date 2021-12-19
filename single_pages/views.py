from django.shortcuts import render

# Create your views here.
from shop.models import Item


def landing(request):
    popular_items = Item.objects.order_by('pk')[:3]
    return render(request, 'single_pages/landing.html',
                  {'popular_items' : popular_items})

def about_us(request):
    return render(request, 'single_pages/about_us.html')