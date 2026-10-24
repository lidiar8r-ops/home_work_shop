from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from catalog.models import Product
from catalog.services import invalidate_product_cache


@receiver([post_save, post_delete], sender=Product)
def clear_product_cache(sender, instance, **kwargs):
    """Сбрасывает кеш продукта и списка категории при изменении или удалении."""
    invalidate_product_cache(instance.pk, instance.category_id)
