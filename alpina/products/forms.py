from django import forms
from .models import Product, Cake


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


class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = [
            'title',
            'pieces',
            'weigth_g',
            'weigth_per_piece_g',
            'product1',
            'product1_quantity',
            'product2',
            'product2_quantity',
            'product3',
            'product4',
            'product5',
            'product6',
            'product7',
            'product8',
            'product9',
            'product10',
            'product11',
            'product12',
            'product13',
            'product14',
            'product15',
            'product16',
            'product17',
            'product18',
            'product19',
            'product20',
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
