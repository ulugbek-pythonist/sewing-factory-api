from rest_framework import serializers

from .models import ProductMaterials, WareHouse


class WareHouseSerilizer(serializers.ModelSerializer):
    material_name = serializers.SerializerMethodField()
    class Meta:
        model = WareHouse
        fields = ["id","material_name","remainder","price"]
    
    def get_material_name(self,obj):
        return obj.material.name
    

class ProductMaterialsSerializer(serializers.ModelSerializer):
    material_name = serializers.SerializerMethodField()
    class Meta:
        model = ProductMaterials
        fields = ["material_name","quantity"]

    def get_material_name(self,obj):
        return obj.material.name