from django.conf import settings
from django.db import migrations, models


def set_default_owner(apps, schema_editor):
    """Назначает владельцем администратора: того, кто завёл, или первого админа."""
    Product = apps.get_model("catalog", "Product")
    User = apps.get_model("users", "User")

    owner = (
        User.objects.filter(is_superuser=True).order_by("pk").first()
        or User.objects.filter(is_staff=True).order_by("pk").first()
    )
    if owner is None:
        owner = User.objects.create(
            email="admin@example.com",
            password="!",
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
    Product.objects.filter(owner__isnull=True).update(owner=owner)


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_product_options_product_status_publication"),
        ("users", "0002_user_token_alter_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.CASCADE,
                related_name="products",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.RunPython(set_default_owner, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                on_delete=models.deletion.CASCADE,
                related_name="products",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]
