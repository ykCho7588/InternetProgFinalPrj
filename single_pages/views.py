from django.shortcuts import render
# Create your views here.
from shop.models import Item
from django.contrib.auth.models import User


def landing(request):
    recent_items = Item.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/landing.html',
                  {'recent_items' : recent_items})

def about_us(request):
    return render(request, 'single_pages/about_us.html')

def my_page(request):
    user_list = User.objects.all()
    return render(request, 'single_pages/my_page.html',
                  {'user_list' : user_list})