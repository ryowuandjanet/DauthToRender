from django import forms
from .models import Yfcase

class YfcaseForm(forms.ModelForm):
    class Meta:
        model = Yfcase
        fields = '__all__'
