from django.core.management import BaseCommand, call_command
from django.db import transaction

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Загружает тестовые категории и продукты из фикстур"

    def handle(self, *args, **options):
        with transaction.atomic():
            Product.objects.all().delete()
            Category.objects.all().delete()

            call_command(
                "loaddata",
                "catalog/categories.json",
                "catalog/products.json",
            )

        self.stdout.write(
            self.style.SUCCESS("Тестовые данные успешно загружены.")
        )