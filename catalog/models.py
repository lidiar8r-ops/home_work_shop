from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(max_length=1000, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name',]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ['name',]