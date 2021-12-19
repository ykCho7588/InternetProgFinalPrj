from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Item, Category
from .forms import CommentForm
# Create your views here.

def new_comment(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Item, pk=pk)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = item
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(item.get_absolute_url())
    else:
        raise PermissionDenied

class ItemCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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
    paginate_by = 5

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
        context['comment_form'] = CommentForm
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


