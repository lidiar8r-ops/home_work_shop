from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product
from users.models import User


class Command(BaseCommand):
    help = "Add products from fixture"

    def handle(self, *args, **options):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Вставляем записи из фикстуры
        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))

        owner, _ = User.objects.get_or_create(
            email="admin@example.com",
            defaults={"is_active": True, "is_staff": True},
        )

        # Вставляем записи
        сategory, _ = Category.objects.get_or_create(
            name="Косметика и гигиена", description="косметические и гигиенические средства "
        )

        products = [
            {
                "name": "Духи Pepper",
                "description": "",
                "image": "",
                "category": сategory,
                "price": 1700,
                "owner": owner,
            },
            {
                "name": "Шампунь Farcom",
                "description": "шампунь",
                "image": "",
                "category": сategory,
                "price": 269.99,
                "owner": owner,
            },
            {
                "name": "Сухой шампунь",
                "description": "шампунь",
                "image": "",
                "category": сategory,
                "price": 169.99,
                "owner": owner,
            },
            {
                "name": "Кондеционер Tresemme",
                "description": "",
                "image": "",
                "category": сategory,
                "price": 280,
                "owner": owner,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added book: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Book already exists: {product.name}"))
