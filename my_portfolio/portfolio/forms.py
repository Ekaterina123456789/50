from django import forms
from .models import Catalog


class WorkForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('title', 'picture', 'description', 'date_completed', 'favourite', 'user')


class ViewForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ['title', 'picture']
