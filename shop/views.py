from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Item
# Create your views here.
class ItemList(ListView):
    model = Item
    ordering = 'pk' # 게시된 순서대로 상품을 보여준다.
#    template_name = 'shop/item_list.html'
#item_list.html
class ItemDetail(DetailView):
    model = Item
#item_detail.html


