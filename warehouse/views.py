from django.db.models import F
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.response import Response

from warehouse.serializers import ProductSerializer
from .models import Product, Warehouse, ProductMaterial


class ProductViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MaterialRequirementsView(APIView):
    def post(self, request, *args, **kwargs):
        product_quantities = request.data.get("products", [])
        response_data = {"result": []}

        warehouse_cache = {wh.id: wh.remainder for wh in Warehouse.objects.all()}

        for pq in product_quantities:
            product_id = pq.get("product_id")
            quantity_required = pq.get("quantity")
            product_response = self.process_product(
                product_id, quantity_required, warehouse_cache
            )
            response_data["result"].append(product_response)

        return Response(response_data)

    def process_product(self, product_id, quantity_required, warehouse_cache):
        product = get_object_or_404(Product, id=product_id)
        materials_needed = ProductMaterial.objects.filter(product=product).annotate(
            required_quantity=F("quantity") * quantity_required
        )

        output = {
            "product_name": product.name,
            "product_qty": quantity_required,
            "product_materials": [],
        }

        for mn in materials_needed:
            material_response = self.process_material(
                mn.material, mn.required_quantity, warehouse_cache
            )
            output["product_materials"].extend(material_response)

        return output

    def process_material(self, material, required_quantity, warehouse_cache):
        warehouses = Warehouse.objects.filter(material=material).order_by("price")

        output = []
        allocated_quantity = 0

        for warehouse in warehouses:
            if allocated_quantity >= required_quantity:
                break

            current_remainder = warehouse_cache[warehouse.id]
            if current_remainder == 0:
                continue

            allocate = min(current_remainder, required_quantity - allocated_quantity)
            allocated_quantity += allocate

            warehouse_cache[warehouse.id] -= allocate

            output.append(
                {
                    "warehouse_id": warehouse.id if allocate > 0 else None,
                    "material_name": material.name,
                    "qty": allocate,
                    "price": warehouse.price if allocate > 0 else None,
                }
            )

        if allocated_quantity < required_quantity:
            output.append(
                {
                    "warehouse_id": None,
                    "material_name": material.name,
                    "qty": required_quantity - allocated_quantity,
                    "price": None,
                }
            )

        return output
