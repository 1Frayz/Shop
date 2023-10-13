from django import forms
from shop.models import Product



class CartAddProductForm(forms.Form):
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)