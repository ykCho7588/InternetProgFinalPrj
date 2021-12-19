from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Item, Category
# Create your views here.

class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['item_name', 'item_info', 'item_price', 'head_image', 'corp_name', 'category', 'item_size', 'item_color']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(ItemCreate, self).form_valid(form)
        else:
            return redirect('/shop/')

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['item_name', 'item_info', 'item_price', 'head_image', 'corp_name', 'category', 'item_size', 'item_color']

    template_name = 'shop/item_update_form.html'

    def dispatch(self, request, *args, **kwargs): #get or post 방식을 구별해주는 함수
        if request.user.is_authenticated and request.user == self.get_object().author : #요청 사용자가 로그인하였고 해당 포스트의 작성자이면
            return super(ItemUpdate, self).dispatch(request, *args, **kwargs)
        else :
            raise PermissionDenied

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

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        item_list = Item.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        item_list = Item.objects.filter(category=category)

    return render(request, 'shop/item_list.html',
                  {
                      'item_list' : item_list,
                      'categories' : Category.objects.all(),
                      'no_category_item_count' : Item.objects.filter(category=None).count(),
                      'category' : category
                  }
                  )


