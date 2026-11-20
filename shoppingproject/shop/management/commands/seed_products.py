
from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = "Add sample products without duplicates"

    def handle(self, *args, **kwargs):
        products = [
            {
                "name": "Wireless Mouse",
                "description": "Ergonomic wireless mouse",
                "price": 599.00,
                "stock": 10,
            },
            {
                "name": "Mechanical Keyboard",
                "description": "RGB mechanical keyboard",
                "price": 1499.00,
                "stock": 5,
            },
            {
                "name": "USB-C Hub",
                "description": "Multiport USB-C adapter",
                "price": 899.00,
                "stock": 8,
            },
        ]

        for item in products:
            Product.objects.get_or_create(
                name=item["name"],
                defaults=item,
            )

        self.stdout.write(
            self.style.SUCCESS("Sample products added successfully!")
        )
