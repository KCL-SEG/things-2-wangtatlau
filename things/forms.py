"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    # Customize the widgets for description and quantity fields
    widgets = {
        'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        'quantity': forms.NumberInput(attrs={'min': 0}),
    }
