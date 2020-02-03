from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('id', 'name', 'price')
        labels = {
            'id': 'Product ID',
            'name': 'Product Name',
            'price': 'Price'
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['min'] = 0