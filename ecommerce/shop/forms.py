from django.forms import widgets, ModelForm
from .models import  ShoppingCartItem

class SaveCartItemForm(ModelForm):
    class Meta:
        model = ShoppingCartItem
        fields = ['quantity']
