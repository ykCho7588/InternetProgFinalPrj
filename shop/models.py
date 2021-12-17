from django.db import models

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
    item_info = models.TextField(verbose_name='상품설명')
    item_price = models.IntegerField(verbose_name='상품가격')

    corp_name = models.ForeignKey(Corp, null=True, on_delete=models.SET_NULL, verbose_name='제조사명')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='카테고리')

    item_size = models.IntegerField(verbose_name='사이즈')
    item_color = models.CharField(max_length=30, verbose_name='색상')

    def __str__(self):
        return f'[{self.pk}]{self.item_name}' #목록 제목 에서 상품명 보여주기.

    def get_absolute_url(self):
        return f'/shop/{self.pk}/'



