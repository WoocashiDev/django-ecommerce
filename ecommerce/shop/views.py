from django.shortcuts import render, redirect
from .models import ShoppingCart, ShoppingCartItem
from users.models import UserProfile
from products.models import Product
from .forms import SaveCartItemForm
from django.contrib import messages


def ShoppingCartPage(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    shopping_cart = ShoppingCart.objects.get(user=profile)
    shopping_cart_items = shopping_cart.shoppingcartitem_set.all()
    form = SaveCartItemForm()

    if request.method == "POST":
        form = SaveCartItemForm(request.POST)
        item_no = 0
        for cart_item in shopping_cart_items:
            print(request.POST)
            cart_item.quantity = request.POST.getlist('quantity')[item_no]
            cart_item.save()
            item_no += 1


    context={
        'shopping_cart': shopping_cart,
        'form': form
        }
    return render(request, 'shop/cart.html', context)


def RemoveCartItemPage(request, item_id):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    shopping_cart = ShoppingCart.objects.get(user=profile)
    shopping_cart_items = shopping_cart.shoppingcartitem_set.all()
    item_to_delete = shopping_cart_items.get(id=item_id)
    item_to_delete.delete()


    return redirect('shopping-cart')


def AddCartItemPage(request, item_id):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    shopping_cart = ShoppingCart.objects.get(user=profile)
    product = Product.objects.get(id=item_id)

    # checking if cart item was added before:
    cart_item =shopping_cart.shoppingcartitem_set.filter(product=product).first()

    
    if cart_item:
        messages.success(request, 'Dodano kolejną sztukę produktu do koszyka')
        cart_item.quantity += 1
        cart_item.save()
    else:
        new_cart_item = ShoppingCartItem.objects.create(
            cart=shopping_cart, product=product, quantity=1, unit_price=product.price
        )
        new_cart_item.save()
        messages.success(request, 'Dodano nowy produkt do koszyka')
    return redirect(request.GET['next'] if 'next' in request.GET else 'products')