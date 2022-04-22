import uuid
from django.db import models
from random import randint, randrange
from apps.products.models import Product
from apps.users.models import CustomUser
from django.core.validators import MinValueValidator


def get_reference():
    reference = randrange(randint(0000000000, 9999999999))
    return reference


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=11)
    paid_amount = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(1)])
    reference = models.CharField(max_length=10, default=get_reference, unique=True, validators=[MinValueValidator(10)])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_on",)
        verbose_name = "order"
        verbose_name_plural= "orders"
    
    def __str__(self):
        return self.product

    