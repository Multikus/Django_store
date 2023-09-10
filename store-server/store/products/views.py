from django.shortcuts import render
from products.models import Product, ProductCategory


# Функция вывода главной страницы.
# Минимальный вариант функции, но её уже можно использовать
def index(request):
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)


# Страница содержит повторяющиеся элементы верстки, карточки товара. Для их отображения используем тег
# который запускает цикл FOR. Предварительно подготовим список со словарями, из этих карточек
def products(request):
    context = {'title': 'Store - Каталог',
               # будем выводить карточки товара через цикл
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all(),
               }
    return render(request, 'products/products.html', context)
