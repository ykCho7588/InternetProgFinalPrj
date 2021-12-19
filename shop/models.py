from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
from markdownx.models import MarkdownxField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) # 한글 허용

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return f'/shop/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'

class Corp(models.Model):
    corp_name = models.CharField(max_length=256, verbose_name='제조사명')
    corp_address = models.CharField(max_length=300, verbose_name='주소')
    corp_tel = models.CharField(max_length=30, verbose_name='연락처')
    corp_ceo = models.CharField(max_length=30, verbose_name='CEO')

    def __str__(self):
        return self.corp_name
    def get_absolute_url(self):
        return f'/shop/corp/{self.slug}'

class Item(models.Model):
    item_name = models.CharField(max_length=256, verbose_name='상품명')
    item_info = MarkdownxField(verbose_name='상품설명')
    item_price = models.IntegerField(verbose_name='상품가격')

    head_image = models.ImageField(upload_to='shop/images/%Y/%m/%d/', null=True, blank=True, verbose_name='상품 이미지')
    corp_name = models.ForeignKey(Corp, null=True, on_delete=models.SET_NULL, verbose_name='제조사명')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='카테고리')

    item_size = models.CharField(max_length=256, verbose_name='사이즈')
    item_color = models.CharField(max_length=30, verbose_name='색상')

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.item_name} :: {self.author}' #목록 제목 에서 상품명 보여주기.

    def get_absolute_url(self):
        return f'/shop/{self.pk}/'

    def get_item_info_markdown(self):
        return markdown(self.item_info)

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'https://doitdjango.com/avatar/id/405/5075a999a10beac9/svg/{self.author.email}/'

class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField() #텍스트의 길이는 제한하지 않음
    created_at = models.DateTimeField(auto_now_add=True) #시간은 자동으로 추가

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.item.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'https://doitdjango.com/avatar/id/405/5075a999a10beac9/svg/{self.author.email}/'


