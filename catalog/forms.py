import os
from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product

class StyleFormMixin:
    DEFAULT_WIDGET_CLASSES = {
        forms.BooleanField: 'form-check-input',
    }
    ADD_PLACEHOLDER = True  # Флаг для добавления placeholder
    REQUIRED_ERROR_MESSAGE = 'Это поле обязательно для заполнения'  # Сообщение об ошибке на русском

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Инициализируем attrs, если его нет
            if not hasattr(field.widget, 'attrs'):
                field.widget.attrs = {}

            # Определяем класс виджета
            widget_class = None
            for field_type, css_class in self.DEFAULT_WIDGET_CLASSES.items():
                if isinstance(field, field_type):
                    widget_class = css_class
                    break

            # Добавляем placeholder, если нужно и есть label
            if self.ADD_PLACEHOLDER and field.label:
                field.widget.attrs['placeholder'] = field.label

            # Специальные настройки для ImageField
            if isinstance(field, forms.ImageField):
                field.widget.attrs['accept'] = 'image/jpeg,image/png'
            elif isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

            # Если поле обязательное и у него ещё нет error_messages
            if field.required:
                if not hasattr(field, 'error_messages'):
                    field.error_messages = {}
                # Добавляем или переопределяем сообщение для 'required'
                field.error_messages['required'] = self.REQUIRED_ERROR_MESSAGE


dict_worlds = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name.lower().strip()
        if not name_l:
            raise forms.ValidationError("Поле не может быть пустым")

        for word in dict_worlds:
            if word in name_l:
                raise ValidationError(f"Слово '{word}' запрещено использовать в названиях.")

        return name


    def clean_description(self):
        description = self.cleaned_data['description']
        description_l = description.lower().strip()
        if description_l in dict_worlds:
            raise ValidationError("Нельзя использовать это слово в описаниях продуктов")
        if not description:  # Это делает поле обязательным!
            raise forms.ValidationError("Поле не может быть пустым")
        return description


    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Цена продукта не может быть отрицательной")


    def clean_image(self):
        image = self.cleaned_data.get('image')

        # Если изображение не загружено — возвращаем None
        if not image:
            return image

        # Проверка размера (5 МБ = 5 242 880 байт)
        max_size = 5 * 1024 * 1024
        if image.size > max_size:
            actual_size_mb = image.size / (1024 * 1024)
            raise ValidationError(
                f'Размер файла слишком большой: {actual_size_mb:.2f} МБ. '
                f'Максимальный размер: 5 МБ'
            )

        # Проверка расширения через os.path
        file_ext = os.path.splitext(image.name)[1].lower()
        allowed_extensions = ['.jpg', '.jpeg', '.png']
        if file_ext not in allowed_extensions:
            raise ValidationError(
                'Недопустимый формат файла. Разрешены: JPEG (.jpg, .jpeg) и PNG (.png)'
            )

        return image
