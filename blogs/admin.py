from django.contrib import admin

from .models import Blog



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'description', 'image', 'publication')
    list_filter = ("title",)
    search_fields = (
        "title",
        "description",
    )


