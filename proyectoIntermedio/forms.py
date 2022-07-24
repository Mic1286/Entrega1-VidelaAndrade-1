from django import forms

class BusquedaCelulares(forms.Form):
    apodo = forms.CharField(max_length=30, required=False)