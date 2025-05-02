from django import forms
from .models import ShopifySettings, Product_Category, Suppliers, Collections, Product

class ShopifySettingsForm(forms.ModelForm):
    class Meta:
        model = ShopifySettings
        fields = ['access_token']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add CSS classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        # special styling for specific fields
        self.fields['description'].widget.attrs.update({'rows': 3})
        self.fields['product_image'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['product_image'].required = False # Make the field optional
        self.fields['barcode'].widget.attrs.update({'placeholder': 'Enter numeric barcode'})