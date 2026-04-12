from django.forms import ModelForm, forms, BooleanField
from prompt_toolkit.validation import ValidationError

from catalog.models import Product

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


dict_worlds = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар", ]


class ProductForm(StyleFormMixin,ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #
        # }


    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name.lower()
        if name_l in  dict_worlds:
            raise forms.ValidationError("Нельзя использовать это слово в названиях продуктов")

    def clean_description(self):
        description = self.cleaned_data['description']
        description_l = description.lower()
        if description_l in dict_worlds :
            raise forms.ValidationError("Нельзя использовать это слово в описаниях продуктов")

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <=0:
            raise forms.ValidationError("Цена продукта не может быть отрицательной")

