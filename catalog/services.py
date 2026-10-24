"""Сервисные функции каталога и работа с кешем Redis."""

from django.conf import settings
from django.core.cache import cache

from catalog.models import Category, Product
from users.models import User

# Логические ключи кеша (django-redis добавит KEY_PREFIX и версию)
CATEGORY_PRODUCTS_CACHE_KEY = "category_{id}"
PRODUCT_DETAIL_CACHE_KEY = "product_detail_{id}"


def get_category_by_key(category_key: str | int) -> Category | None:
    """Ищет категорию по числовому id или по slug. Возвращает None, если не найдена."""
    key = str(category_key).strip()
    queryset = Category.objects.all()
    if key.isdigit():
        return queryset.filter(pk=int(key)).first()
    return queryset.filter(slug=key).first()


def get_product(product_id: int) -> Product | None:
    """Продукт из Redis; при промахе — из БД с записью в кеш."""
    cache_key = PRODUCT_DETAIL_CACHE_KEY.format(id=product_id)
    product = cache.get(cache_key)
    if product is None:
        product = Product.objects.select_related("category").filter(pk=product_id).first()
        if product is not None:
            cache.set(cache_key, product, settings.PRODUCT_DETAIL_CACHE_TTL)
    return product


def get_products_by_category(category: Category) -> list[Product]:
    """Список продуктов категории с низкоуровневым кешем category_{id}."""
    cache_key = CATEGORY_PRODUCTS_CACHE_KEY.format(id=category.pk)
    products = cache.get(cache_key)
    if products is None:
        products = list(
            Product.objects.filter(category=category).select_related("category").order_by("name")
        )
        cache.set(cache_key, products, settings.CATEGORY_PRODUCTS_CACHE_TTL)
    return products


def invalidate_product_cache(product_id: int, category_id: int) -> None:
    """Сбрасывает кеш продукта и списка его категории."""
    cache.delete(PRODUCT_DETAIL_CACHE_KEY.format(id=product_id))
    cache.delete(CATEGORY_PRODUCTS_CACHE_KEY.format(id=category_id))


def get_default_owner(user=None):
    """Владелец по умолчанию: кто создаёт запись, иначе первый администратор."""
    if user is not None and getattr(user, "is_authenticated", False):
        return user
    return (
        User.objects.filter(is_superuser=True).order_by("pk").first()
        or User.objects.filter(is_staff=True).order_by("pk").first()
    )
