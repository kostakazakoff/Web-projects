from django.db import models
from django.urls import reverse


class Product(models.Model):
    CHOICES = (
    ('л.', 'л.'),
    ('кг.', 'кг.'),
    ('кв/ч.', 'кв/ч.'),
    ('бр.', 'бр.'),
    ('мин.', 'мин.')
    )
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Наименование')
    price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=False, default=0, verbose_name='Цена')
    unit = models.CharField(max_length=10, blank=True, null=True, choices=CHOICES, verbose_name='Мярка')
    comment = models.TextField(max_length=200, default=None, blank=True, null=True, verbose_name='Забележка')

    def get_absolute_url(self):
        return reverse('products', kwargs={'id': self.id})

    def __str__(self):
        return self.title


class ComplexProduct(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Наименование')
    products = models.ManyToManyField(Product, related_name='complex_products', verbose_name='Продукти')
    price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=False, default=0, verbose_name='Цена')
    unit = models.CharField(max_length=10, blank=True, null=True, verbose_name='Мярка')
    comment = models.TextField(max_length=200, default=None, blank=True, null=True, verbose_name='Забележка')

    def get_absolute_url(self):
        return reverse('complex_products', kwargs={'id': self.id})

    def __str__(self):
        return self.title


class Article(models.Model):
    ARTICLE_TYPES = (
        ('cake', 'Торта'),
        ('peace_of_cake', 'Паста'),
        ('other', 'Други'),
        ('complex_product', 'Заготовка'),
    )

    products_choices = [(x.title, x.title) for x in Product.objects.all()]
    complex_products_choices = [(x.title, x.title) for x in ComplexProduct.objects.all()]
    products_choices += complex_products_choices

    article_type = models.CharField(max_length=100, blank=False, null=False, choices=ARTICLE_TYPES, verbose_name='Вид')
    title = models.CharField(max_length=200, blank=False, null=False, unique=True, verbose_name='Наименование')
    pieces = models.IntegerField(blank=True, null=True, default=16, verbose_name='Брой')
    weigth_g = models.IntegerField(blank=True, null=True, default=0, verbose_name='Тегло')
    weigth_per_piece_g = models.IntegerField(editable=False, blank=True, null=True, default=0, verbose_name='Тегло/бр.')

    product1 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product1_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product2 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product2_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product3 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product3_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product4 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product4_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product5 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product5_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product6 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product6_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product7 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product7_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product8 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product8_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product9 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product9_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product10 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product10_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product11 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product11_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product12 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product12_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product13 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product13_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product14 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product14_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product15 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product15_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product16 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product16_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product17 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product17_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product18 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product18_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product19 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product19_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')
    product20 = models.CharField(max_length=100, blank=True, null=True, choices=products_choices, verbose_name='Продукт')
    product20_quantity = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0, verbose_name='Количество')

    # products = models.ManyToManyField(Product, related_name='articles', choices=products_choices, blank=True, verbose_name='Продукти')
    # complex_products = models.ManyToManyField(ComplexProduct, related_name='articles', choices=complex_products_choices, blank=True, verbose_name='Заготовки')

    electricity = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Ток')
    water = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Вода')
    worker_expenses = models.DecimalField(decimal_places=2, max_digits=10, blank=False, default=0, null=False, verbose_name='Работа')
    package = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Опаковки')
    fuel = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Гориво')

    cost_price = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Себестойност')

    other_expenses = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Други разходи 10%')
    manufacturing_costs = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Производствени загуби 8%')

    final_costs_price = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='Общо себестойност')

    workshop_profit = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=False, default=0, null=False, verbose_name='Печалба цех 10%')
    workshop_price = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=False, default=0, null=False, verbose_name='Цена цех')
    vat = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=False, null=False, default=0, verbose_name='ДДС')
    price_incl_vat = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=False, default=0, null=False, verbose_name='Стойност с ДДС')
    price_incl_vat_per_piece = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=False, default=0, null=False, verbose_name='Стойност с ДДС')

    # sell_price = models.DecimalField(decimal_places=2, max_digits=10, blank=False, default=0, null=False, verbose_name='Продажна цена - всички')
    # sell_price_for_piece = models.DecimalField(decimal_places=2, max_digits=10, default=0, blank=False, null=False, verbose_name='Продажна цена - брой')

    comment = models.TextField(max_length=200, default=None, blank=True, null=True, verbose_name='Забележка')

    reciep = models.TextField(max_length=5000, default=None, blank=True, null=True, verbose_name='Рецепта')
    cake_image = models.ImageField(blank=True, null=True, verbose_name='Снимка')

    def get_absolute_url(self):
        return reverse('articles', kwargs={'id': self.id})

    def __str__(self):
        return self.title