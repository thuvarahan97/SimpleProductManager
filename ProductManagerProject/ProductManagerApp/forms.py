from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')
        labels = {
            'id': 'Product ID',
            'name': 'Product Name',
            'price': 'Price'
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['min'] = 0
        self.fields['id'].widget.attrs['placeholder'] = 'Enter Product ID'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Product Name'
        self.fields['price'].widget.attrs['placeholder'] = 'Enter Product Price'
