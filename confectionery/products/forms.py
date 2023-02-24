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
            'quantity',
            'comment',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'unit': forms.Select(attrs={'class': 'input-field'}),
            'quantity': forms.Select(attrs={'class': 'input-field'}),
            'comment': forms.Textarea(attrs={'class': 'input-field'}),
            'price': forms.NumberInput(attrs={'class': 'input-field'}),
        }


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