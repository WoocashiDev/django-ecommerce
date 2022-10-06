from django.shortcuts import render, redirect
from .models import ShoppingCart, ShoppingCartItem
from users.models import UserProfile, UserAddress
from products.models import Product, TopCategory
from .forms import SaveCartItemForm
from users.forms import UserAddressForm
from django.contrib import messages


def ShoppingCartPage(request):
    top_categories = TopCategory.objects.all()
    user = request.user
    profile = UserProfile.objects.get(user=user)
    shopping_cart = ShoppingCart.objects.get(user=profile)
    shopping_cart_items = shopping_cart.shoppingcartitem_set.all()
    form = SaveCartItemForm()

    if request.method == "POST":
        form = SaveCartItemForm(request.POST)
        item_no = 0
        for cart_item in shopping_cart_items:
            cart_item.quantity = request.POST.getlist('quantity')[item_no]
            cart_item.unit_price = cart_item.product.price
            cart_item.total_price = cart_item.product.price * int(cart_item.quantity)
            
            cart_item.save()
            item_no += 1
        return redirect('checkout')


    context={
        'shopping_cart': shopping_cart,
        'form': form,
        'top_categories': top_categories
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

    # setting default quantity as 1
    item_quantity = 1

    # taking quantity from the form posted from product-details page
    if request.method == "POST":
        item_quantity = int(request.POST['quantity'])
        print(item_quantity)

    # checking if item is already in the cart
    if cart_item:
        messages.success(request, 'Dodano kolejną sztukę produktu do koszyka')
        cart_item.quantity += item_quantity
        cart_item.save()
    
    # if not, new item is being created
    else:
        new_cart_item = ShoppingCartItem.objects.create(
            cart=shopping_cart, product=product, quantity=item_quantity, unit_price=product.price
        )
        new_cart_item.save()
        messages.success(request, 'Dodano nowy produkt do koszyka')
    return redirect(request.GET['next'] if 'next' in request.GET else 'products')



def CheckoutPage(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    cart = ShoppingCart.objects.get(user=profile)

    cart_items = cart.shoppingcartitem_set.all()
    final_price = 0
    for item in cart_items:
        final_price += item.total_price
    

    # checking if user address exists in the database
    try:
        user_address = UserAddress.objects.get(profile=profile)
    
    # creating user address object if it is non-existent
    except:
        user_address = UserAddress.objects.create(
            profile=profile
        )

    form = UserAddressForm(instance=user_address)

    if request.method == 'POST':
        form = UserAddressForm(request.POST, instance=user_address)
        if form.is_valid():
            form.save()
            return redirect('checkout')


    context={
        'form': form,
        'cart': cart,
        'final_price': final_price
    }
    return render(request, 'shop/checkout.html', context)