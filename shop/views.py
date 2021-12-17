from django.shortcuts import render
from .models import Item
# Create your views here.
def index(request):
    items = Item.objects.all().order_by('pk') #게시된 순서대로

    return render(request, 'shop/index.html',
                  {
                      'items' : items
                  }
                  )
def single_item_page(request, pk):
    item = Item.objects.get(pk=pk)

    return render(request, 'shop/single_item_page.html',
                  {
                      'item': item
                  }
                  )
