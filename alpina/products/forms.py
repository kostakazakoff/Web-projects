from django import forms
from .models import Product, Article


# all_products = Product.objects.all()
# context = [(p.title, p.title) for p in all_products]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title',
                'price',
                'unit',
                'comment']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'article_type',
            'title',
            'pieces',
            'weigth_g',
            'product_01',
            'product_01_quantity',
            # 'product_02',
            # 'product_02_quantity',
            # 'product_03',
            # 'product_03_quantity',
            # 'product_04',
            # 'product_04_quantity',
            # 'product_05',
            # 'product_05_quantity',
            # 'product_06',
            # 'product_06_quantity',
            # 'product_07',
            # 'product_07_quantity',
            # 'product_08',
            # 'product_08_quantity',
            # 'product_09',
            # 'product_09_quantity',
            # 'product_10',
            # 'product_10_quantity',
            # 'product_11',
            # 'product_11_quantity',
            # 'product_12',
            # 'product_12_quantity',
            # 'product_13',
            # 'product_13_quantity',
            # 'product_14',
            # 'product_14_quantity',
            # 'product_15',
            # 'product_15_quantity',
            # 'product_16',
            # 'product_16_quantity',
            # 'product_17',
            # 'product_17_quantity',
            # 'product_18',
            # 'product_18_quantity',
            # 'product_19',
            # 'product_19_quantity',
            # 'product_20',
            # 'product_20_quantity',
            'electricity',
            'water',
            'worker_expenses',
            'package',
            'fuel',
            'comment',
            'reciep',
            'cake_image'
            ]
