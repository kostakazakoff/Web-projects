from django.contrib import admin
from .models import Product, Article, Ingredient


admin.site.register(Product)
admin.site.register(Article)
admin.site.register(Ingredient)