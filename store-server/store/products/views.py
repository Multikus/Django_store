from django.shortcuts import render


# Функция вывода главной страницы.
# Минимальный вариант функции, но её уже можно использовать
def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')
