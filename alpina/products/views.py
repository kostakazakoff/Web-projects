from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse


# def home_view(request):
#     context = {}
#     all_products = Product.objects.all()
#     context['products'] = [p.title for p in all_products]

#     return render(request, 'home.html', context)


def cakes_list(request):
    context = {}
    return render(request, 'cakes/cakes_list.html', context)


@login_required
def products_list(request):
    operation = request.GET.get('operation')
    search_text = ''
    if operation == 'Search':
        search_text = request.GET.get('search').lower()
        

    context = {
        'title': 'Продукти:',
        'products': [],
    }
    queryset = Product.objects.all()
    context['products'] = [p for p in queryset if search_text in p.title.lower()]

    return render(request, 'products/products_list.html', context)


@login_required
def product_details(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    print(request.POST)
    operation = request.POST.get('operation')
    if operation == 'Save':
        if form.is_valid():
            form.save()
            return redirect('/../products_list')
    elif operation == 'Delete':
        obj.delete()
        return redirect('/../products_list')
    context = {
        'form': form,
    }
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

        print()
        print(operation)

    return render(request, 'home.html', {})
