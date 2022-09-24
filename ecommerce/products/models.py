from unicodedata import name
from django.db import models
import uuid

# Create your models here.

class ProductBrand(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class TopCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class MidCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    top_category = models.ForeignKey(TopCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class BotCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    mid_category = models.ForeignKey(MidCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ProductStock(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=True, blank=True)

    @property
    def in_stock(self):
        is_in_stock = False
        if self.quantity == 0:
            is_in_stock=False
        else:
            is_in_stock=True
        
        return is_in_stock


class ProductTag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    brand = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True)
    bot_category = models.ManyToManyField(BotCategory, blank=False)
    stock = models.ManyToManyField(ProductStock, blank=True)
    tags = models.ManyToManyField(ProductTag, blank=True)

    def __str__(self):
        return ' '.join((self.name+self.size))


class ProductImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default='default.jpg')
    is_featured = models.BooleanField(default=False, blank=True, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return ' '.join((self.product.name, self.id))