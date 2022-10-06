from django.forms import widgets, ModelForm
from .models import Product

class ProductSearchForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name']
