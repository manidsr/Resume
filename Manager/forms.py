from django import forms

class identitityFrom(forms.Form):
    name = forms.CharField(max_length=100)