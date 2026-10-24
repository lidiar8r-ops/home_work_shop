from django.db import models
from django.utils.text import slugify

from config import settings
from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    # unique намеренно не задан: Django 6 дублирует pattern-index для unique SlugField.
    # Уникальность slug обеспечивает save().
    slug = models.SlugField(
        max_length=120,
        blank=True,
        verbose_name="Слаг",
        help_text="Используется в URL; заполняется автоматически из названия",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._make_unique_slug()
        super().save(*args, **kwargs)

    def _make_unique_slug(self):
        base = slugify(self.name, allow_unicode=True) or "category"
        slug = base
        suffix = 1
        queryset = Category.objects.exclude(pk=self.pk)
        while queryset.filter(slug=slug).exists():
            suffix += 1
            slug = f"{base}-{suffix}"
        return slug

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = [
            "name",
        ]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    image = models.ImageField(upload_to="image/", verbose_name="Изображение", blank=True, null=True,
                              help_text='Загрузите изображение в формате JPEG или PNG, не более 5 МБ')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories", verbose_name="Категория"
    )
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    status_publication = models.BooleanField(default=False, verbose_name="Статус публикации")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Владелец',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = [
            "name",
        ]
        permissions = [
            ('can_unpublish_product','can unpublish product'),
        ]


class Contact(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Адрес")
    working_hours = models.CharField(
        max_length=100, verbose_name="Часы работы", help_text="Например: Пн-Пт 9:00–18:00"
    )

    def __str__(self):
        return f"Контакты: {self.phone}"

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"
