from django.db.models import CharField, ForeignKey, FloatField, DecimalField, CASCADE

from root.models import BaseModel


class Material(BaseModel):
    name = CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    name = CharField(max_length=256)
    barcode = CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class ProductMaterial(BaseModel):
    product = ForeignKey(Product, on_delete=CASCADE, related_name="usage_materials")
    material = ForeignKey(Material, on_delete=CASCADE, related_name="usage_products")
    quantity = FloatField()

    class Meta:
        unique_together = ("product", "material")


class Warehouse(BaseModel):
    material = ForeignKey(Material, on_delete=CASCADE)
    remainder = FloatField()
    price = DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.material.name} | Partiya {self.pk}"
