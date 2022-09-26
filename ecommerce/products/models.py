from email.policy import default
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
    category_image = models.ImageField(null=True, blank=True, default='categories/default.jpg', upload_to="categories")

    def __str__(self):
        return self.name

class MidCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    top_category = models.ForeignKey(TopCategory, on_delete=models.CASCADE, null=True)
    category_image = models.ImageField(null=True, blank=True, default='categories/default.jpg', upload_to="categories")

    def __str__(self):
        return self.name

class BotCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    mid_category = models.ForeignKey(MidCategory, on_delete=models.CASCADE, null=True)
    category_image = models.ImageField(null=True, blank=True, default='categories/default.jpg', upload_to="categories")

    def __str__(self):
        return self.name


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
    size = models.CharField(max_length=10, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    old_price = models.FloatField(null=True, blank=True)
    promoted = models.BooleanField(null=True, blank=True, default=False)
    brand = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True)
    bot_category = models.ManyToManyField(BotCategory, blank=False)
    stock = models.IntegerField(null=True, blank=True)
    tags = models.ManyToManyField(ProductTag, blank=True)

    def __str__(self):
        return f"{self.name} {str(self.size)}"
    
    @property
    def in_stock(self):
        is_in_stock = False
        if self.stock == 0:
            is_in_stock=False
        else:
            is_in_stock=True
        
        return is_in_stock


class ProductImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default='products/default.jpg', upload_to="products")
    is_featured = models.BooleanField(default=False, blank=True, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return ' '.join((self.product.name, self.product.size))