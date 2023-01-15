from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Наименование')
    price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=False, default=0, verbose_name='Цена')
    unit = models.CharField(max_length=10, blank=True, null=True, verbose_name='Мярка')
    comment = models.TextField(max_length=200, default=None, blank=True, null=True, verbose_name='Забележка')

    def get_absolute_url(self):
        return reverse('products', kwargs={'id': self.id})

    def __str__(self):
        return self.title


class Cake(models.Model):
    choices = [(x.title, x.title) for x in Product.objects.all()]
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Вид')
    pieces = models.IntegerField(blank=False, null=False, default=16, verbose_name='Брой')
    weigth_g = models.IntegerField(blank=False, null=False, default=0, verbose_name='Тегло')
    weigth_per_piece_g = models.IntegerField(blank=False, null=False, default=0, verbose_name='Тегло/бр.')

    product1 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product1_quantity = models.DecimalField(decimal_places=3, max_digits=10, default=0, blank=False, null=False)
    product2 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product2_quantity = models.DecimalField(decimal_places=3, max_digits=10, default=0, blank=False, null=False)
    
    product3 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product4 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product5 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product6 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product7 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product8 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product9 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product10 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product11 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product12 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product13 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product14 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product15 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product16 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product17 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product18 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product19 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')
    product20 = models.CharField(max_length=100, blank=True, null=True, choices=choices, verbose_name='Продукт')

    electricity = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Ток')
    water = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Вода')
    worker_expenses = models.DecimalField(decimal_places=2, max_digits=10, blank=False, default=0, null=False, verbose_name='Работа')
    package = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Опаковки')
    fuel = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Гориво')

    cost_price = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, verbose_name='Себестойност')

    other_expenses = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Други разходи 10%')
    manufacturing_costs = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Производствени загуби 8%')

    final_costs_price = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, verbose_name='Общо себестойност')

    workshop_profit = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, verbose_name='Печалба цех 10%')
    workshop_price = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, verbose_name='Цена цех')
    vat = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, verbose_name='ДДС')
    price_incl_vat = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, verbose_name='Стойност с ДДС')

    sell_price = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, verbose_name='Продажна цена - всички')
    sell_price_for_piece = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, verbose_name='Продажна цена - брой')

    comment = models.TextField(max_length=200, default=None, blank=True, null=True, verbose_name='Забележка')

    reciep = models.TextField(max_length=5000, default=None, blank=True, null=True, verbose_name='Рецепта')
    cake_image = models.ImageField(blank=True, null=True, verbose_name='Снимка')

    def get_absolute_url(self):
        return reverse('cakes', kwargs={'id': self.id})

    def __str__(self):
        return self.title