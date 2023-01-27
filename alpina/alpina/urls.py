"""alpina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import products_list, product_details, create_product, login_view, articles_list, create_article, article_details

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_view, name='home'),
    path('products_list/', products_list, name='products'),
    path('articles_list/', articles_list, name='articles'),
    path('products/<int:id>/', product_details, name='product_details'),
    path('articles/<int:id>/', article_details, name='article_details'),
    path('create_product/', create_product, name='create_product'),
    path('create_article/', create_article, name='create_article'),
    path('', login_view, name='login'),
]
