from django import forms
from .models import Product


# all_products = Product.objects.all()
# context = [(p.title, p.title) for p in all_products]

class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Наименование'}))
    price = forms.DecimalField(decimal_places=2)
    unit = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Мерна единица'}))
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Бележки',
                'rows': 10,
                'cols': 40,
            }
        )
    )
    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'unit',
            'comment',
        ]

