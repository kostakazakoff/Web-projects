from django import forms
from .models import Product, Article


# all_products = Product.objects.all()
# context = [(p.title, p.title) for p in all_products]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'unit',
            'comment',
        ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'pieces',
            'weigth_g',
            'weigth_per_piece_g',
            # 'products',
            # 'complex_products',
            'electricity',
            'water',
            'worker_expenses',
            'package',
            'fuel',
            'cost_price',
            'other_expenses',
            'manufacturing_costs',
            'final_costs_price',
            'workshop_profit',
            'workshop_price',
            'vat',
            'cake_image',
        ]
