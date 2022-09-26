from django.shortcuts import render
from .models import Product, TopCategory, ProductTag, ProductBrand, ProductImage, MidCategory, BotCategory
import random

# Create your views here.
def productsMainPage(request):
    top_categories = TopCategory.objects.all()
    all_promoted_products = Product.objects.filter(promoted=True).all()
    products_list = [product for product in all_promoted_products]
    print(products_list)
    random.shuffle(products_list)
    print(products_list)
    if len(products_list) >= 8:
        promoted_products = products_list[0:8]
    else:
        promoted_products = products_list

   

    context = {
        "top_categories": top_categories,
        "promoted_products": promoted_products}
    return render(request, 'products/products-main.html', context)

def productsCollectionPage(request, category_id):
    top_categories = TopCategory.objects.all()
    products = Product.objects.filter(bot_category=category_id).all()
    print(products)
    context = {
        'products': products,
        "top_categories": top_categories
        }
    return render(request, 'products/products-collection.html', context)

def productsCategoryCollectionPage(request, category_id):
    top_categories = TopCategory.objects.all()
    top_category = TopCategory.objects.get(id=category_id)
    mid_categories = top_category.midcategory_set.all()

    context = {
        "categories": mid_categories,
        "top_categories": top_categories
    }
    return render(request, 'products/products-categories-collection.html', context)

def productsSubCategoryCollectionPage(request, category_id):
    top_categories = TopCategory.objects.all()
    mid_category = MidCategory.objects.get(id=category_id)
    bot_categories = mid_category.botcategory_set.all()

    context = {
        "categories": bot_categories,
        "top_categories": top_categories
    }
    return render(request, 'products/products-subcategories-collection.html', context)