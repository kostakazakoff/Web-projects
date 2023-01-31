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


# class ArticleCreateForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = [
#             'article_type',
#             'title',
#             ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'article_type',
            'title',
            'pieces',
            'weigth_g',
            'product1',
            'product1_quantity',
            'product2',
            'product2_quantity',
            'product3',
            'product3_quantity',
            'product4',
            'product4_quantity',
            'product5',
            'product5_quantity',
            'product6',
            'product6_quantity',
            'product7',
            'product7_quantity',
            'product8',
            'product8_quantity',
            'product9',
            'product9_quantity',
            'product10',
            'product10_quantity',
            'product11',
            'product11_quantity',
            'product12',
            'product12_quantity',
            'product13',
            'product13_quantity',
            'product14',
            'product14_quantity',
            'product15',
            'product15_quantity',
            'product16',
            'product16_quantity',
            'product17',
            'product17_quantity',
            'product18',
            'product18_quantity',
            'product19',
            'product19_quantity',
            'product20',
            'product20_quantity',

            'electricity',
            'water',
            'worker_expenses',
            'package',
            'fuel',
            'comment',
            'reciep',
            'cake_image'
            ]


# class ArticleAddProductsForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = [
#             'products',
#             'complex_products',
#             ]