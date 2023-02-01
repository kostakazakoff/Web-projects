from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product, Article, Ingredient
from .forms import ProductForm, ArticleForm, IngredientForm, ArticleCreateForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


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
    search_product = request.GET.get('search_product') if request.GET.get('search_product') else None

    context = {'title': 'Продукти:',
        'products': [p for p in queryset]}

    if search_product:
        context['products'] = [p for p in queryset if int(search_product) == p.id]

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

ingredients = []

@login_required
def create_article(request):
    article_form = ArticleCreateForm(request.POST or None)
    context = {'article_form': article_form}

    if article_form.is_valid():
        article_form.save()
        print(article_form.data)
        obj = Article.objects.last()
        obj_id = obj.id
        print(obj_id)
        context = {'article': obj}
        return redirect(f'/../articles/{obj.id}')
    
    # article = get_object_or_404(Article, title=article_form.data['title'])
    # ingredient = get_object_or_404(Ingredient, title=ingredient_form.data['title'])
    

        

    # if article_form.is_valid():
    #     article_form.save()
    #     article = get_object_or_404(Article, title=article_form.data['title'])

    #     article.weigth_per_piece_g = article.weigth_g // article.pieces

        # ingredients_total_cost = sum([Decimal(k.price) * Decimal(v) for k, v in ingredients.items() if k])
        # article.cost_price = ingredients_total_cost + article.electricity + article.water \
        #                      + article.worker_expenses + article.package + article.fuel
        # article.other_expenses = article.cost_price * Decimal(0.1)
        # article.manufacturing_costs = article.cost_price * Decimal(0.08)
        # article.final_costs_price = article.cost_price + article.other_expenses + article.manufacturing_costs
        # article.workshop_profit = article.final_costs_price * Decimal(0.1)
        # article.workshop_price = article.final_costs_price + article.workshop_profit
        # article.vat = article.workshop_price * Decimal(0.2)
        # article.price_incl_vat = article.workshop_price + article.vat
        # article.price_incl_vat_per_piece = article.price_incl_vat / article.pieces

        # article.save()

        # context = {'article_form': article_form, 'ingredient_form': ingredient_form, 'article': article}

    return render(request, 'articles/create_article.html', context)


@login_required
def article_details(request, id):
    article = get_object_or_404(Article, id=id)
    article_form = ArticleForm(request.POST or None, instance=article)
    ingredient_form = IngredientForm(request.POST or None)
    operation = request.POST.get('operation')
    
    if operation == 'add_ingredient':
        if ingredient_form.is_valid():
            ingredient_form.save()
            ingredient_form = IngredientForm()
            ingredient = Ingredient.objects.last()
            ingredients.append(ingredient)
    
    elif operation == 'create_article':
        if article_form.is_valid():
            article.ingredients.add(ingredients)

    context = {'article_form': article_form, 'ingredient_form': ingredient_form, 'article': article}
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
