from django.db import models

class Product(models.Model):
    PAYMENT_CHOICE = [("ON", "ONLINE"),("COD", "Cash On Delievery")]
    product_name = models.CharField(max_length = 20)
    product_price = models.IntegerField()
    product_quan = models.IntegerField()
    delivery_address = models.CharField(max_length = 20)
    payment_mode = models.CharField(max_length=3, choices = PAYMENT_CHOICE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)

