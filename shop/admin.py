from django.contrib import admin
from .models import Item, Corp, Category
# Register your models here.
admin.site.register(Item)
admin.site.register(Corp)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category',)}
admin.site.register(Category, CategoryAdmin)