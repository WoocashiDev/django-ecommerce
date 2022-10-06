from django.shortcuts import render
from .models import Product, TopCategory, ProductTag, ProductBrand, ProductImage, MidCategory, BotCategory
import random
from shop.forms import SaveCartItemForm
from django.views.generic import ListView
from .forms import ProductSearchForm
import re

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

def productDetailsPage(request, product_id):
    top_categories = TopCategory.objects.all()
    product = Product.objects.get(id=product_id)
    images = product.productimage_set.all()
    product_category = product.bot_category.first()
    same_category_products = Product.objects.filter(bot_category = product_category)

    form = SaveCartItemForm()

    context = {
        "top_categories": top_categories,
        "form": form,
        "product": product,
        "images": images,
        "same_category_products": same_category_products
    }
    return render(request, 'products/product-detail.html', context)


class ProductSearchView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ProductSearchForm(self.request.GET)

        if form.is_valid():

            name = form['name'].value()

        if name:
                queryset = queryset.filter(
                    name__icontains=name
                )
        
        return super().get_context_data(
            object_list=queryset,
            **kwargs
        )

        # fixing issues with pagination and filtering
    def setup(self, request, *args, **kwargs) -> None:
        request.GET.get("page")
        request.META["QUERY_STRING"] = re.sub("(&|\?)page=(.)*", "", request.META.get("QUERY_STRING", ""))
        return super().setup(request, *args, **kwargs)