from django import forms
from .models import productDetails

class productDetailsForm(forms.ModelForm):
    class Meta:
        model= productDetails
        fields='__all__'

