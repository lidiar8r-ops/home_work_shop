from django.db import models
from django.shortcuts import render

# Create your views here.

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(max_length=1000, verbose_name="Содержимое")
    image = models.ImageField(upload_to="image/", verbose_name="Изображение", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    publication = models.BooleanField(auto_now=True, verbose_name="Признак публикации",default=False)
    counter_views = models.IntegerField(verbose_name="количество просмотров", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = [
            "title",
        ]


