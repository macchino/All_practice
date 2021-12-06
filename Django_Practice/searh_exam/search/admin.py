from django.contrib import admin
from search.models import Tag, Category, Item
# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Item)
