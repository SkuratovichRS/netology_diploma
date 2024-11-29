from django.db import models

# Order
# user
# dt
# status
# OrderItem
# order
# product
# shop
# quantity
# Contact
# type
# user
# value


class Order(models.Model):
    dt = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return f"Order #{self.id}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Список заказов"
        ordering = ("dt",)


class OrderItem(models.Model):
    quantity = models.IntegerField(null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders_items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="orders_items")
    shop = models.ForeignKey("products.Shop", on_delete=models.CASCADE, related_name="orders_items")

    def __str__(self):
        return f"Order item #{self.id}"

    class Meta:
        verbose_name = "Детали заказа"
        verbose_name_plural = "Список деталей заказов"
        ordering = ("order",)

class Contact(models.Model):
    type = models.CharField(max_length=150, null=False)
    value = models.CharField(max_length=150, null=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="contacts")

    def __str__(self):
        return f"Contact #{self.id}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Список контактов"
        ordering = ("user",)