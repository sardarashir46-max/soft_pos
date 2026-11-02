
from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):

    status = forms.TypedChoiceField(
        choices=[
            ('True', 'Active'),
            ('False', 'Inactive')
        ],
        coerce=lambda value: value == 'True',
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Category

        fields = ['name', 'status']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            })
        }
