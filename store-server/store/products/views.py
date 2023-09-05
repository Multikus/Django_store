from django.shortcuts import render


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
               'products': [
                       {
                           'images': '../static/vendor/img/products/Adidas-hoodie.png',
                           'name': 'Худи черного цвета с монограммами adidas Originals',
                           'price': 6090,
                           'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                       },
                       {
                           'images': '../static/vendor/img/products/Blue-jacket-The-North-Face.png',
                           'name': 'Синяя куртка The North Face',
                           'price': 23725,
                           'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                       },
                       {
                           'images': '../static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                           'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                           'price': 3390,
                           'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                       }
                    ],
               }
    return render(request, 'products/products.html', context)
