"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import ProductSearchView

urlpatterns = [
    path('', views.productsMainPage, name="products"),
    path('category/<str:category_id>', views.productsCollectionPage, name="category"),
    path('category-collection/<str:category_id>', views.productsCategoryCollectionPage, name="category-collection"),
    path('subcategory-collection/<str:category_id>', views.productsSubCategoryCollectionPage, name="subcategory-collection"),
    path("product-details/<str:product_id>/", views.productDetailsPage, name="product-details"),
    path('products-search/', ProductSearchView.as_view(), name='products-search'),
]