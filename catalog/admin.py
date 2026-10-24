from django.contrib import admin

from catalog.services import get_default_owner
from users.models import User
from .models import Category, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    search_fields = (
        "id",
        "name",
        "slug",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "owner")
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )
    exclude = ("owner",)

    def save_model(self, request, obj, form, change):
        # Владелец по умолчанию — тот, кто создаёт продукт
        if not obj.owner_id:
            obj.owner = get_default_owner(request.user)
        super().save_model(request, obj, form, change)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')
    search_fields = ('phone', 'email', 'address')
    list_filter = ('working_hours',)



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", 'email')
