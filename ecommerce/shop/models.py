from random import choices
from django.db import models
from users.models import UserProfile
from products.models import Product
import uuid


# Create your models here.
class ShoppingCart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"Cart: {self.user.username}"
    
class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True, blank=False, default=1)
    unit_price = models.FloatField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"Cart item:{self.product.name}"
