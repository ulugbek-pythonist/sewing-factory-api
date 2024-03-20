from django.core.management.base import BaseCommand
from warehouse.models import Material, Product, ProductMaterial, Warehouse


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Materials
        material1 = Material.objects.get_or_create(name="Mato")[0]
        material2 = Material.objects.get_or_create(name="Ip")[0]
        material3 = Material.objects.get_or_create(name="Tugma")[0]
        material4 = Material.objects.get_or_create(name="Zamok")[0]

        # Products
        product1 = Product.objects.get_or_create(name="Ko'ylak", barcode="123")[0]
        product2 = Product.objects.get_or_create(name="Shim", barcode="456")[0]

        # Product-Material links
        ProductMaterial.objects.get_or_create(
            product=product1, material=material1, quantity=0.8
        )
        ProductMaterial.objects.get_or_create(
            product=product1, material=material3, quantity=5
        )
        ProductMaterial.objects.get_or_create(
            product=product1, material=material2, quantity=10
        )

        ProductMaterial.objects.get_or_create(
            product=product2, material=material1, quantity=1.4
        )
        ProductMaterial.objects.get_or_create(
            product=product2, material=material2, quantity=15
        )
        ProductMaterial.objects.get_or_create(
            product=product2, material=material4, quantity=1
        )

        # Warehouse stock
        Warehouse.objects.get_or_create(material=material1, remainder=12, price=1500)
        Warehouse.objects.get_or_create(material=material1, remainder=200, price=1600)
        Warehouse.objects.get_or_create(material=material2, remainder=40, price=500)
        Warehouse.objects.get_or_create(material=material2, remainder=300, price=550)
        Warehouse.objects.get_or_create(material=material3, remainder=500, price=300)
        Warehouse.objects.get_or_create(material=material4, remainder=1000, price=2000)

        self.stdout.write(self.style.SUCCESS("Database populated successfully."))
