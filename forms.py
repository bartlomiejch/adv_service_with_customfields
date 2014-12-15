from django import forms
from .models import Category



class AdvForm(forms.Form):
    dupa = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
