from django.contrib import admin
from .models import Product, Article, ComplexProduct


admin.site.register(Product)
admin.site.register(Article)
admin.site.register(ComplexProduct)