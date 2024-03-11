from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Product, Material, ProductMaterials, WareHouse


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["name","bar_code"]


@admin.register(Material)
class MaterialAdmin(ModelAdmin):
    list_display = ["name",]


@admin.register(ProductMaterials)
class ProductMaterialsAdmin(ModelAdmin):
    list_display = ["product","material","quantity"]


@admin.register(WareHouse)
class WareHouseAdmin(ModelAdmin):
    list_display = ["id","material","remainder","price"]

