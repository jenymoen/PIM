from django import forms
from .models import ShopifySettings, Product_Category, Suppliers, Collections, Product

class ShopifySettingsForm(forms.ModelForm):
    class Meta:
        model = ShopifySettings
        fields = ['access_token']