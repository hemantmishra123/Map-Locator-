from django import forms
from .models import Search


class SearchForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Enter Username'}))

    class Meta:
        model = Search
        fields = ['address', ]
