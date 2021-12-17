from django.contrib import admin
from .models import Item, Corp, Category
# Register your models here.
admin.site.register(Item)
admin.site.register(Corp)
admin.site.register(Category)