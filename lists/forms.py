from django import forms

from .models import Item

EMPTY_LIST_ERROR = "Element nie może być pusty"


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': "Wpisz rzecz do zrobienia",
                'class': 'form-control input-lg'
            })
        }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }
