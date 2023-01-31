from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product, Article, ComplexProduct
from .forms import ProductForm, ArticleForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal
# from django.http import HttpResponse


# def home_view(request):
#     context = {}
#     all_products = Product.objects.all()
#     context['products'] = [p.title for p in all_products]

#     return render(request, 'home.html', context)


@login_required
def articles_list(request):
    operation = request.GET.get('operation')
    search_text = ''
    if operation == 'search':
        search_text = request.GET.get('search').lower()
    context = {
        'articles': [],
    }
    queryset = Article.objects.all().order_by('title')
    context['articles'] = [
        p for p in queryset if search_text in p.title.lower()]
    return render(request, 'articles/articles_list.html', context)


@login_required
def products_list(request):
    queryset = Product.objects.all().order_by('title')
    search_product = request.GET.get(
        'search_product') if request.GET.get('search_product') else None

    context = {
        'title': 'Продукти:',
        'products': [p for p in queryset],
    }

    if search_product:
        context['products'] = [
            p for p in queryset if int(search_product) == p.id]

    return render(request, 'products/products_list.html', context)


@login_required
def product_details(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    operation = request.POST.get('operation')
    if operation == 'Save':
        if form.is_valid():
            form.save()
            return redirect('/../products_list')
    elif operation == 'Delete':
        obj.delete()
        return redirect('/../products_list')
    context = {'form': form}
    return render(request, 'products/product_details.html', context)


@login_required
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        return redirect('/../products_list')
    context = {'form': form}

    return render(request, 'products/product_create.html', context)


@login_required
def create_article(request):
    form = ArticleForm(request.POST or None)
    article_id = None

    if form.is_valid():
        form.save()
        article = get_object_or_404(Article, title=form.data['title'])
        article_id = article.id

        article.weigth_per_piece_g = article.weigth_g // article.pieces

        ingredients = {
            Product.objects.get(title=article.product1) if article.product1 else None: article.product1_quantity if article.product1_quantity else 0,
            Product.objects.get(title=article.product2) if article.product2 else None: article.product2_quantity if article.product2_quantity else 0,
            Product.objects.get(title=article.product3) if article.product3 else None: article.product3_quantity if article.product3_quantity else 0,
            Product.objects.get(title=article.product4) if article.product4 else None: article.product4_quantity if article.product4_quantity else 0,
            Product.objects.get(title=article.product5) if article.product5 else None: article.product5_quantity if article.product5_quantity else 0,
            Product.objects.get(title=article.product6) if article.product6 else None: article.product6_quantity if article.product6_quantity else 0,
            Product.objects.get(title=article.product7) if article.product7 else None: article.product7_quantity if article.product7_quantity else 0,
            Product.objects.get(title=article.product8) if article.product8 else None: article.product8_quantity if article.product8_quantity else 0,
            Product.objects.get(title=article.product9) if article.product9 else None: article.product9_quantity if article.product9_quantity else 0,
            Product.objects.get(title=article.product10) if article.product10 else None: article.product10_quantity if article.product10_quantity else 0,
            Product.objects.get(title=article.product11) if article.product11 else None: article.product11_quantity if article.product11_quantity else 0,
            Product.objects.get(title=article.product12) if article.product12 else None: article.product12_quantity if article.product12_quantity else 0,
            Product.objects.get(title=article.product13) if article.product13 else None: article.product13_quantity if article.product13_quantity else 0,
            Product.objects.get(title=article.product14) if article.product14 else None: article.product14_quantity if article.product14_quantity else 0,
            Product.objects.get(title=article.product15) if article.product15 else None: article.product15_quantity if article.product15_quantity else 0,
            Product.objects.get(title=article.product16) if article.product16 else None: article.product16_quantity if article.product16_quantity else 0,
            Product.objects.get(title=article.product17) if article.product17 else None: article.product17_quantity if article.product17_quantity else 0,
            Product.objects.get(title=article.product18) if article.product18 else None: article.product18_quantity if article.product18_quantity else 0,
            Product.objects.get(title=article.product19) if article.product19 else None: article.product19_quantity if article.product19_quantity else 0,
            Product.objects.get(title=article.product20) if article.product20 else None: article.product20_quantity if article.product20_quantity else 0,
        }

        ingredients_total_cost = sum([Decimal(k.price) * Decimal(v) for k, v in ingredients.items() if k])
        article.cost_price = ingredients_total_cost + article.electricity + article.water \
                             + article.worker_expenses + article.package + article.fuel
        article.other_expenses = article.cost_price * Decimal(0.1)
        article.manufacturing_costs = article.cost_price * Decimal(0.08)
        article.final_costs_price = article.cost_price + article.other_expenses + article.manufacturing_costs
        article.workshop_profit = article.final_costs_price * Decimal(0.1)
        article.workshop_price = article.final_costs_price + article.workshop_profit
        article.vat = article.workshop_price * Decimal(0.2)
        article.price_incl_vat = article.workshop_price + article.vat
        article.price_incl_vat_per_piece = article.price_incl_vat / article.pieces

        article.save()

        # return redirect(f'/../articles/{int(article.id)}')

    context = {'form': form, 'article': article}

    return render(request, 'articles/create_article.html', context)


@login_required
def article_details(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=article)

    context = {'form': form, 'article': article}
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
                return redirect('/../products_list')
            else:
                return redirect('/')
        elif operation == 'Logout':
            logout(request)

    return render(request, 'home.html', {})
