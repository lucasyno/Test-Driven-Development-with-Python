from django import forms
from django.core.exceptions import ValidationError

from .models import Item

EMPTY_LIST_ERROR = "Element nie może być pusty"
DUPLICATE_ITEMS_ERROR = "Podany element już istnieje na liście"


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

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()


class ExistingListItemForm(ItemForm):

    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEMS_ERROR]}
            self._update_errors(e)

    def save(self):
        return forms.ModelForm.save(self)
