from django.contrib import admin
from .models import Product, TopCategory, ProductTag, ProductBrand, ProductImage, MidCategory, BotCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(TopCategory)
admin.site.register(ProductTag)
admin.site.register(ProductBrand)
admin.site.register(ProductImage)
admin.site.register(MidCategory)
admin.site.register(BotCategory)