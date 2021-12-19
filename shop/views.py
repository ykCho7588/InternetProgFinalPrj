from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Item, Category
# Create your views here.
class ItemList(ListView):
    model = Item
    ordering = 'pk' # 게시된 순서대로 상품을 보여준다.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_item_count'] = Item.objects.filter(category=None).count()
        return context

class ItemDetail(DetailView):
    model = Item

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_item_count'] = Item.objects.filter(category=None).count()
        return context



