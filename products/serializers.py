from products.models import Category, Parameter, Product, ProductInfo, ProductParameter, Shop


class ImportSerializer:
    def create_shop(self, name: str) -> Shop:
        return Shop.objects.get_or_create(name=name)[0]

    def create_category(self, id: int, name: str) -> Category:
        return Category.objects.get_or_create(id=id, name=name)[0]

    def create_product(self, product_id: int, name: str, category_id: int) -> Product:
        category = Category.objects.get(id=category_id)
        return Product.objects.create(id=product_id, name=name, category=category)

    def create_product_info(
        self, name: str, quantity: int, price: float, price_rrc: float, product: Product, shop: Shop
    ) -> ProductInfo:
        return ProductInfo.objects.create(
            name=name, quantity=quantity, price=price, price_rrc=price_rrc, product=product, shop=shop
        )

    def create_parameter(self, name: str) -> Parameter:
        return Parameter.objects.create(name=name)

    def create_product_parameter(
        self, value: str, parameter: Parameter, product_info: ProductInfo
    ) -> ProductParameter:
        return ProductParameter.objects.create(value=value, parameter=parameter, product_info=product_info)
