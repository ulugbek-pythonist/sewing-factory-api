from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ProductMaterialsSerializer, WareHouseSerilizer

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

        data = []

        for pm in serializer.data:
            pm["quantity"] = float(pm["quantity"]) * quantity1
            data.append(pm)

        return Response(
            {
                "result": [
                    {
                        "product_name": product1,
                        "product_qty": quantity1,
                        "product_materials":data
                    },
                    {
                        "product_name": product2,
                        "product_qty": quantity2,
                        "product_materials":None
                    }
                ]
            }
        )
