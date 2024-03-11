from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ProductMaterialsSerializer, WareHouseSerilizer, WareHouseSpecialSerilizer

from .models import ProductMaterials, WareHouse


class HealtCheckView(APIView):

    def get(self, request):
        return Response(
            {"message": "Everything is OK, let's go on"}, status.HTTP_200_OK
        )


class GetRemaindersAPIView(APIView):

    def get(self, request):
        batches = WareHouse.objects.all()

        serializer = WareHouseSerilizer(batches, many=True)

        data = []

        for batch in serializer.data:
            data.append(batch)

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        product1 = request.data.get("product1")
        quantity1 = request.data.get("quantity1")
        quantity2 = request.data.get("quantity2")
        product2 = request.data.get("product2")

        product1_materials = ProductMaterials.objects.filter(product__name=product1)
        serializer = ProductMaterialsSerializer(product1_materials,many=True)

        data1 = []

        for pm in serializer.data:
            pm["quantity"] = float(pm["quantity"]) * quantity1
            data1.append(pm)

        product2_materials = ProductMaterials.objects.filter(product__name=product2)
        serializer = ProductMaterialsSerializer(product2_materials,many=True)

        data2 = []

        for pm in serializer.data:
            pm["quantity"] = float(pm["quantity"]) * quantity2
            data2.append(pm)

        data1 = self.simple_calculation(data1,0) + self.simple_calculation(data1,1) + self.simple_calculation(data1,2)
        data2 = self.simple_calculation(data2,0) + self.simple_calculation(data2,1) + self.simple_calculation(data2,2)

        return Response(
            {
                "result": [
                    {
                        "product_name": product1,
                        "product_qty": quantity1,
                        "product_materials":data1
                    },
                    {
                        "product_name": product2,
                        "product_qty": quantity2,
                        "product_materials":data2
                    }
                ]
            }
        )
    
    def simple_calculation(self,data,indeks):
        material = data[indeks]

        warehouse_material = WareHouse.objects.filter(material__name=material["material_name"])

        serializer = WareHouseSpecialSerilizer(warehouse_material,many=True)
        info = []
        for warehouse_info in serializer.data:
            if material["quantity"] <= warehouse_info["remainder"]:
                warehouse_info["remainder"] -= material["quantity"]
                qty = material["quantity"]
                adding = {
                    "warehouse_id": warehouse_info["id"],
                    "material_name": warehouse_info["material_name"],
                    "qty": qty,
                    "price": warehouse_info["price"]
                    }
                info.append(adding)
                material["quantity"] = 0
                break
            else:
                adding = {
                    "warehouse_id": warehouse_info["id"],
                    "material_name": warehouse_info["material_name"],
                    "qty": warehouse_info["remainder"],
                    "price": warehouse_info["price"]
                    }
                material["quantity"] -= warehouse_info["remainder"]
                info.append(adding)
                warehouse_info["remainder"] = 0

        adding = {
                    "warehouse_id": None,
                    "material_name": warehouse_info["material_name"],
                    "qty": material["quantity"] ,
                    "price": None
                    }
        
        if material["quantity"] > 0:
            info.append(adding)
            
        return info
