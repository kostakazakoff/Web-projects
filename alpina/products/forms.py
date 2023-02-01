from django import forms
from .models import Product, Article, Ingredient


# all_products = Product.objects.all()
# context = [(p.title, p.title) for p in all_products]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title',
                'price',
                'unit',
                'comment']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['title',
                'product',
                'quantity']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'article_type',
            'title',
            'pieces',
            'weigth_g',
            'electricity',
            'water',
            'worker_expenses',
            'package',
            'fuel',
            'comment',
            'reciep',
            'cake_image'
            ]

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_type',
                'title',]