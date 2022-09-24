from django.shortcuts import render
from .models import Product, TopCategory, ProductStock, ProductTag, ProductBrand, ProductImage, MidCategory, BotCategory

# Create your views here.
def productsMainPage(request):
    top_categories = TopCategory.objects.all()

    context = {"top_categories": top_categories}
    return render(request, 'products/products-main.html', context)