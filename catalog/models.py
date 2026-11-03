from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Наименование",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        verbose_name="Изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class Contact(models.Model):
    country = models.CharField(
        max_length=100,
        verbose_name="Страна",
    )
    tax_number = models.CharField(
        max_length=30,
        verbose_name="ИНН",
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес",
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"