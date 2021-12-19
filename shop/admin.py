from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Item, Corp, Category
# Register your models here.
admin.site.register(Item, MarkdownxModelAdmin)
admin.site.register(Corp)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category',)}
admin.site.register(Category, CategoryAdmin)