from django.shortcuts import render

# Create your views here.
def shopMainPage(request):
    context = {}
    return render(request, 'shop/shop-main.html', context)