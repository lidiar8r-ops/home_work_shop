from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #
        # }