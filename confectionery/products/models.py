from django.db import models
from django.urls import reverse


class Units(models.TextChoices):
        kg = 'кг.', 'кг.'
        l = 'л.', 'л.'
        pc = 'бр.', 'бр.'
        min = 'мин.', 'мин.'
        kw_h = 'кв/ч.', 'кв/ч.'


class ArticleTypes(models.TextChoices):
    cake = 'cake', 'Торта'
    peace_of_cake = 'peace_of_cake', 'Паста'
    other = 'other', 'Други'


class Product(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, unique=True, verbose_name='Наименование')
    price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=False, default=0, verbose_name='Цена')
    unit = models.CharField(max_length=10, blank=True, null=True, choices=Units.choices, default=Units.pc, verbose_name='Мярка')
    quantity = models.DecimalField(decimal_places=3, max_digits=10, default=0, blank=True, null=True, verbose_name='Количество')
    comment = models.TextField(max_length=200, default=None, blank=True, null=True, verbose_name='Забележка')

    def get_absolute_url(self):
        return reverse('products', kwargs={'id': self.id})

    def __str__(self):
        return self.title
    

class ComplexProduct(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, unique=True, verbose_name='Наименование')
    products = models.ManyToManyField(Product, verbose_name='Продукти')
    unit = models.CharField(max_length=10, blank=True, null=True, choices=Units.choices, verbose_name='Мярка')
    quantity = models.DecimalField(decimal_places=3, max_digits=10, default=0, blank=True, null=True, verbose_name='Количество')
    comment = models.TextField(max_length=200, default=None, blank=True, null=True, verbose_name='Забележка')

    def get_absolute_url(self):
        return reverse('complex_products', kwargs={'id': self.id})

    def __str__(self):
        return self.title


class Article(models.Model):
    
    
    products_choice = [(x.title, x.title) for x in Product.objects.all()]
    article_type = models.CharField(max_length=100, blank=True, null=False, choices=ArticleTypes.choices, default=ArticleTypes.cake, verbose_name='Вид')
    title = models.CharField(max_length=200, blank=False, null=False, unique=True, verbose_name='Наименование')
    pieces = models.IntegerField(blank=True, null=True, default=16, verbose_name='Брой')
    weigth_g = models.IntegerField(blank=True, null=True, default=0, verbose_name='Тегло')
    weigth_per_piece_g = models.IntegerField(editable=False, blank=True, null=True, default=0, verbose_name='Тегло/бр.')

    products = models.ManyToManyField(Product, verbose_name='Продукти')
    complex_products = models.ManyToManyField(ComplexProduct, verbose_name='Продукти')

    electricity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Ток')
    water = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Вода')
    worker_expenses = models.DecimalField(decimal_places=2, max_digits=10, blank=True, default=0, null=False, verbose_name='Работа')
    package = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Опаковки')
    fuel = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Гориво')
    cost_price = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Себестойност')
    other_expenses = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Други разходи 10%')
    manufacturing_costs = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Производствени загуби 8%')
    final_costs_price = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Общо себестойност')
    workshop_profit = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=True, default=0, null=False, verbose_name='Печалба цех 10%')
    workshop_price = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=True, default=0, null=False, verbose_name='Цена цех')
    vat = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='ДДС')
    price_incl_vat = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=True, default=0, null=False, verbose_name='Стойност с ДДС')
    price_incl_vat_per_piece = models.DecimalField(editable=None, decimal_places=2, max_digits=10, blank=True, default=0, null=False, verbose_name='Стойност с ДДС')
    comment = models.TextField(max_length=200, default=None, blank=True, null=True, verbose_name='Забележка')
    reciep = models.TextField(max_length=5000, default=None, blank=True, null=True, verbose_name='Рецепта')
    cake_image = models.ImageField(blank=True, null=True, verbose_name='Снимка')

    def get_absolute_url(self):
        return reverse('articles', kwargs={'id': self.id})

    def __str__(self):
        return self.title