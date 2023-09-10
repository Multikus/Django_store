from django.db import models


# Создаем модель для таблицы с категориями.
# Чтобы джанго понимал, что нам нужно создать модель, мы должны наш класс наследовать от класса models.Model
class ProductCategory(models.Model):
    # Описываем поля таблицы. Каждая переменная, это поле таблицы.
    # Для работы необходимо описать типы каждой переменной
    # Для данного типа необходимо указать длину текста
    name = models.CharField(max_length=128, unique=True)  # unique=True - поле должно быть уникальным
    # Данный тип для большого текста без необходимости указывать кол-во символов
    description = models.TextField(null=True, blank=True)  # null=True, blank=True - говорят о том, что поле может
    # быть пустым и не заполняться

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    #  DecimalField - поле для работы с ценой. Необходимо указать два параметра
    # max_digits=6 - сколько символов до запятой, decimal_places=2 - сколько символов после запятой
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # числовое поле, но которое может быть = 0 или больше. Меньше никогда
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    # ForeignKey - специальный тип который позволяет связать с другой таблицей.
    # В качестве аргумента передаем имя класса с которым связываем.
    # on_delete=models.CASCADE - необходимо указывать. Параметр указывает, что делать при удалении категории.
    # CASCADE - Будут удалены все товары входящие в эту категорию
    # PROTECT - Нельзя будет удалить, пока не удалишь все товары категории
    # SET_DEFAULT - Если удаляется категория, то подставляется значение по умолчанию.
    # Для этого также нужно указать значение по умолчанию, дополнительным параметром
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
