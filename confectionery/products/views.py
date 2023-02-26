from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product, Article, ComplexProduct
from .forms import ProductForm, ArticleForm, ComplexProductForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


@login_required
def home(request):
    articles_queryset = Article.objects.all().order_by('title')
    products_queryset = Product.objects.all().order_by('title')
    complex_products_queryset = ComplexProduct.objects.all().order_by('title')
    articles = [a for a in articles_queryset]
    products = [p for p in products_queryset]
    complex_products = [cp for cp in complex_products_queryset]

    search_article = request.GET.get(
        'search_article') if request.GET.get('search_article') else None
    search_product = request.GET.get(
        'search_product') if request.GET.get('search_product') else None
    search_complex_product = request.GET.get(
        'search_complex_product') if request.GET.get('search_complex_product') else None
    if search_article:
        articles = [a for a in articles if int(search_article) == a.id]
    if search_product:
        products = [p for p in products if int(search_product) == p.id]
    if search_complex_product:
        complex_products = [cp for cp in complex_products if int(
            search_complex_product) == cp.id]

    article_details = request.GET.get(
        'article-details') if request.GET.get('article-details') else None
    if article_details:
        return redirect(f'./articles/{int(article_details)}')

    product_details = request.GET.get(
        'product-details') if request.GET.get('product-details') else None
    if product_details:
        return redirect(f'./products/{product_details}')

    complex_product_details = request.GET.get(
        'complex-product-details') if request.GET.get('complex-product-details') else None
    if complex_product_details:
        return redirect(f'./complex_products/{int(complex_product_details)}')

    context = {'articles': articles, 'products': products,
               'complex-products': complex_products}
    return render(request, 'home.html', context)


@login_required
def product_details(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    operation = request.POST.get('operation')
    if operation == 'Save':
        if form.is_valid():
            form.save()
            return redirect('/')
    elif operation == 'Delete':
        obj.delete()
        return redirect('/')
    context = {'form': form}
    return render(request, 'products/product_details.html', context)


def calc_complex_product_price(id):
    complex_product = ComplexProduct.objects.get(pk=id)
    ingredients = complex_product.get_ingredients()
    complex_product.price = sum(k.price * v for k, v in ingredients.items()) / complex_product.quantity
    complex_product.save()
    
    # complex_product_ingredients = [
    #     [[i.price for i in ingredients if i.title ==
    #       complex_product.product_01][0], complex_product.product_01_quantity],
    #     [[i.price for i in ingredients if i.title ==
    #       complex_product.product_02][0], complex_product.product_02_quantity],
    #     [[i.price for i in ingredients if i.title ==
    #       complex_product.product_03][0], complex_product.product_03_quantity],
    #     [[i.price for i in ingredients if i.title ==
    #       complex_product.product_04][0], complex_product.product_04_quantity],
    #     [[i.price for i in ingredients if i.title ==
    #       complex_product.product_05][0], complex_product.product_05_quantity],
    #     [[i.price for i in ingredients if i.title ==
    #       complex_product.product_06][0], complex_product.product_06_quantity],
    #     [[i.price for i in ingredients if i.title ==
    #       complex_product.product_07][0], complex_product.product_07_quantity],
    #     [[i.price for i in ingredients if i.title ==
    #       complex_product.product_08][0], complex_product.product_08_quantity],
    #     [[i.price for i in ingredients if i.title ==
    #       complex_product.product_09][0], complex_product.product_09_quantity],
    #     [[i.price for i in ingredients if i.title ==
    #       complex_product.product_10][0], complex_product.product_10_quantity],
    # ]
    # complex_product.price = sum(
    #     [x[0] * x[1] for x in complex_product_ingredients]) * Decimal(1.2)
    # complex_product.save()


@login_required
def complex_product_details(request, id):
    obj = get_object_or_404(ComplexProduct, id=id)
    form = ComplexProductForm(request.POST or None, instance=obj)
    operation = request.POST.get('operation')
    if operation == 'Save':
        if form.is_valid():
            form.save()
            calc_complex_product_price(id)
            return redirect('/')
    elif operation == 'Delete':
        obj.delete()
        return redirect('/')
    context = {'form': form, 'complex_product': obj}
    return render(request, 'products/complex_product_details.html', context)


@login_required
def create_product(request):
    form = ProductForm(request.POST or None)

    operation = request.POST.get('operation')
    if operation == 'Cancel':
        return redirect('/')

    if form.is_valid():
        form.save()
        form = ProductForm()
        return redirect('/')

    context = {'form': form}
    return render(request, 'products/product_create.html', context)


@login_required
def create_complex_product(request):
    form = ComplexProductForm(request.POST or None)
    ingredients = [i for i in Product.objects.all()]
    operation = request.POST.get('operation')
    context = {
        'form': form,
    }

    if operation:
        if operation == 'Save':
            if form.is_valid():
                form.save()
                complex_product = ComplexProduct.objects.last()
                calc_complex_product_price(complex_product['id'])
                return redirect(f'/complex_products/{complex_product["id"]}')

    return render(request, 'products/create_complex_product.html', context)


# ingredients = []

@login_required
def create_article(request):
    article_form = ArticleForm(request.POST or None)

    # if article_form.is_valid():
    #     article_form.save()
    #     # print(article_form.data)
    #     obj = Article.objects.last()
    #     obj_id = obj.id
    #     # print(obj_id)
    #     context = {'article': obj}
    #     return redirect(f'/../articles/{obj.id}')

    # article = get_object_or_404(Article, title=article_form.data['title'])

    if article_form.is_valid():
        print(article_form.cleaned_data)
        article_form.save()
        article = Article.objects.last()

        article.weigth_per_piece_g = article.weigth_g // article.pieces

        ingredients_total_cost = 0

        article.cost_price = ingredients_total_cost + article.electricity + article.water \
            + article.worker_expenses + article.package + article.fuel
        article.other_expenses = article.cost_price * Decimal(0.1)
        article.manufacturing_costs = article.cost_price * Decimal(0.08)
        article.final_costs_price = article.cost_price + \
            article.other_expenses + article.manufacturing_costs
        article.workshop_profit = article.final_costs_price * Decimal(0.1)
        article.workshop_price = article.final_costs_price + article.workshop_profit
        article.vat = article.workshop_price * Decimal(0.2)
        article.price_incl_vat = article.workshop_price + article.vat
        article.price_incl_vat_per_piece = article.price_incl_vat / article.pieces

        article.save()

        context = {'article_form': article_form, 'article': article}

        return redirect('/')

    context = {'article_form': article_form}
    print('Not valid form')

    return render(request, 'articles/create_article.html', context)


@login_required
def article_details(request, id):
    article = get_object_or_404(Article, id=id)
    article_form = ArticleForm(request.POST or None, instance=article)
    operation = request.POST.get('operation')

    if operation == 'create_article':
        if article_form.is_valid():
            print('OK')
            # article.ingredients.add(ingredients)

    context = {'article_form': article_form, 'article': article}
    return render(request, f'articles/article_details.html', context)


def login_view(request):
    if request.method == "POST":
        operation = request.POST.get('operation')
        if operation == 'Login':
            username = request.POST.get('uname')
            password = request.POST.get('pass')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/')
        elif operation == 'Logout':
            logout(request)

    return render(request, 'login-page.html', {})
