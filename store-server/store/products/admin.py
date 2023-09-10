from django.contrib import admin

# Импортируем таблицы
from products.models import ProductCategory, Product

# регистрируем модель
admin.site.register(Product)
admin.site.register(ProductCategory)
