from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Product, Material, ProductMaterial, Warehouse


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["name", "barcode"]


@admin.register(Material)
class MaterialAdmin(ModelAdmin):
    list_display = ["name"]


@admin.register(ProductMaterial)
class ProductMaterialsAdmin(ModelAdmin):
    list_display = ["product", "material", "quantity"]


@admin.register(Warehouse)
class WareHouseAdmin(ModelAdmin):
    list_display = ["id", "material", "remainder", "price"]
