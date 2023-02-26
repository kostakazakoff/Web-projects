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
    comment = models.TextField(max_length=200, default=None, blank=True, null=True, verbose_name='Забележка')

    def get_absolute_url(self):
        return reverse('products', kwargs={'id': self.id})

    def __str__(self):
        return self.title


class ComplexProduct(models.Model):
    p_choices = [(p.title, p.title) for p in Product.objects.all()]
    title = models.CharField(max_length=200, blank=False, null=False, unique=True, verbose_name='Наименование')
    # products = models.ManyToManyField(Product, verbose_name='Продукти')

    product_01 = models.CharField(max_length=100, choices=p_choices, blank=True, null=True, verbose_name='Съставка')
    product_01_quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Количество')
    product_02 = models.CharField(max_length=100, choices=p_choices, blank=True, null=True, verbose_name='Съставка')
    product_02_quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Количество')
    product_03 = models.CharField(max_length=100, choices=p_choices, blank=True, null=True, verbose_name='Съставка')
    product_03_quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Количество')
    product_04 = models.CharField(max_length=100, choices=p_choices, blank=True, null=True, verbose_name='Съставка')
    product_04_quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Количество')
    product_05 = models.CharField(max_length=100, choices=p_choices, blank=True, null=True, verbose_name='Съставка')
    product_05_quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Количество')
    product_06 = models.CharField(max_length=100, choices=p_choices, blank=True, null=True, verbose_name='Съставка')
    product_06_quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Количество')
    product_07 = models.CharField(max_length=100, choices=p_choices, blank=True, null=True, verbose_name='Съставка')
    product_07_quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Количество')
    product_08 = models.CharField(max_length=100, choices=p_choices, blank=True, null=True, verbose_name='Съставка')
    product_08_quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Количество')
    product_09 = models.CharField(max_length=100, choices=p_choices, blank=True, null=True, verbose_name='Съставка')
    product_09_quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Количество')
    product_10 = models.CharField(max_length=100, choices=p_choices, blank=True, null=True, verbose_name='Съставка')
    product_10_quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=0, verbose_name='Количество')

    quantity = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=False, default=1, verbose_name='Количество на заготовката')
    unit = models.CharField(max_length=10, blank=True, null=True, choices=Units.choices, default=Units.pc, verbose_name='Мярка')
    comment = models.TextField(max_length=200, default=None, blank=True, null=True, verbose_name='Забележка')
    price = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=False, default=0, editable=None, verbose_name='Цена')

    def get_absolute_url(self):
        return reverse('complex_products', kwargs={'id': self.id})

    def __str__(self):
        return self.title
    
    def get_ingredients(self):
        ingredients = {}
        all = {
            Product.objects.get(title=self.product_01): self.product_01_quantity,
            Product.objects.get(title=self.product_02): self.product_02_quantity,
            Product.objects.get(title=self.product_03): self.product_03_quantity,
            Product.objects.get(title=self.product_04): self.product_04_quantity,
            # Product.objects.get(title=self.product_05): self.product_05_quantity,
            # Product.objects.get(title=self.product_06): self.product_06_quantity,
            # Product.objects.get(title=self.product_07): self.product_07_quantity,
            # Product.objects.get(title=self.product_08): self.product_08_quantity,
            # Product.objects.get(title=self.product_09): self.product_09_quantity,
            # Product.objects.get(title=self.product_10): self.product_10_quantity,
            }
        for k,v in all.items():
            if k:
                ingredients.update({k: v})
        return ingredients


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