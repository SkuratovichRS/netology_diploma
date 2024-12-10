import yaml
from django.db.utils import IntegrityError
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from products.permissions import IsShopPermission
from products.serializers import ImportSerializer


class ImportView(APIView):

    def get_permissions(self):
        return [IsAuthenticated(), IsShopPermission()]

    def post(self, request: Request) -> Response:
        file = request.FILES.get("file").read().decode("utf-8")
        if not file:
            return Response(data={"error": "No file provided"}, status=400)
        serializer = ImportSerializer()
        data = yaml.safe_load(file)

        try:
            shop_object = serializer.create_shop(data["shop"])
            for category in data["categories"]:
                serializer.create_category(category["id"], category["name"])
            for product in data["goods"]:
                try:
                    product_object = serializer.create_product(product["id"], product["name"], product["category"])
                    product_info_object = serializer.create_product_info(
                        product["model"],
                        product["quantity"],
                        product["price"],
                        product["price_rrc"],
                        product_object,
                        shop_object,
                    )
                    for parameter_name, parameter_value in product["parameters"].items():
                        parameter_object = serializer.create_parameter(parameter_name)
                        serializer.create_product_parameter(parameter_value, parameter_object, product_info_object)
                except IntegrityError:
                    continue

        except KeyError:
            return Response(data={"error": "Invalid file format"}, status=400)

        return Response(data={"message": "File imported successfully"}, status=201)
