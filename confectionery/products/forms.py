from django import forms
from .models import Product, Article, ComplexProduct


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title',
                'price',
                'unit',
                'comment']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'price': forms.NumberInput(attrs={'class': 'input-field'}),
            'unit': forms.Select(attrs={'class': 'input-field'}),
            'comment': forms.Textarea(attrs={'class': 'input-field'}),
        }


class ComplexProductForm(forms.ModelForm):
    class Meta:
        model = ComplexProduct
        fields = [
            'title',
            'unit',
            'comment',
            'product_01',
            'product_01_quantity',
            'product_02',
            'product_02_quantity',
            'product_03',
            'product_03_quantity',
            'product_04',
            'product_04_quantity',
            'product_05',
            'product_05_quantity',
            'product_06',
            'product_06_quantity',
            'product_07',
            'product_07_quantity',
            'product_08',
            'product_08_quantity',
            'product_09',
            'product_09_quantity',
            'product_10',
            'product_10_quantity',
            'unit',
            'quantity',
            'comment',
        ]

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'input-field'}),
        #     'product_01': forms.Select(attrs={'class': 'input-field'}),
        #     'product_01_quantity': forms.NumberInput(attrs={'class': 'input-field'}),
        #     'unit': forms.Select(attrs={'class': 'input-field'}),
        #     'comment': forms.Textarea(attrs={'class': 'input-field'}),
        # }


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
        
        widgets = {
            'article_type': forms.Select(attrs={'class': 'input-field'}),
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'pieces': forms.NumberInput(attrs={'class': 'input-field'}),
            'weigth_g': forms.NumberInput(attrs={'class': 'input-field'}),
            'electricity': forms.NumberInput(attrs={'class': 'input-field'}),
            'water': forms.NumberInput(attrs={'class': 'input-field'}),
            'worker_expenses': forms.NumberInput(attrs={'class': 'input-field'}),
            'package': forms.NumberInput(attrs={'class': 'input-field'}),
            'fuel': forms.NumberInput(attrs={'class': 'input-field'}),
            'comment': forms.Textarea(attrs={'class': 'input-field'}),
            'reciep': forms.Textarea(attrs={'class': 'input-field'}),
            'cake_image': forms.URLInput(attrs={'class': 'input-field'}),
        }