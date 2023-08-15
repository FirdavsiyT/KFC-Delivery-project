from django import forms
from . models import FoodModel


class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodModel()
        exclude = ['id', 'created_at', 'updated_at']