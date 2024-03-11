from django.db import models

from root.models import BaseModel


class Material(BaseModel):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=256)
    bar_code = models.CharField(max_length=100)
    materials = models.ManyToManyField(Material, through='ProductMaterials')

    def __str__(self) -> str:
        return self.name



class ProductMaterials(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="products")
    material = models.ForeignKey(Material,on_delete=models.CASCADE, related_name="materials")
    quantity = models.FloatField()

    class Meta:
        verbose_name_plural = "Product Materials"


class WareHouse(BaseModel):
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    remainder = models.FloatField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self) -> str:
        return f"{self.material.name} | Partiya {self.pk}"
    
    class Meta:
        verbose_name_plural = "Warehouses"