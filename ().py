# coding: utf-8
from catalog.models import Category, Product
mailing = Category.objects.create(
    name="Рассылки",
    description="Сервисы для отправки сообщений",
)
bots = Category.objects.create(
    name="Телеграм-боты",
    description="Боты для автоматизации задач",
)
mailing
mail_service = Product.objects.create(
    name="Сервис рассылок",
    description="Отправка писем клиентам",
    category=mailing,
    price="1400.00",
)
reminder_bot = Product.objects.create(
    name="Бот-напоминатель",
    description="Напоминает о важных событиях",
    category=bots,
    price="900.00",
)
test_product = Product.objects.create(
    name="Тестовый продукт",
    description="Этот продукт удалим для задания",
    category=bots,
    price="100.00",
)
Category.objects.all()
Category.objects.filter(name__icontains="бот")
Product.objects.all()
Product.objects.filter(category=bots)
mail_service.price = "1600.00"
mail_service.save()
Product.objects.get(pk=mail_service.pk).price
