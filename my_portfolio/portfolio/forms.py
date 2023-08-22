from django import forms
from .models import Catalog


class WorkForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('title', 'date', 'picture', 'description')
