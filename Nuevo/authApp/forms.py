from django import forms
from .models import HR

class HRForm(forms.ModelForm):
    class Meta:
        model = HR
        fields = ['name']
