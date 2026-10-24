from django.db import migrations, models
from django.utils.text import slugify


def fill_slugs(apps, schema_editor):
    """Заполняет slug существующих категорий из названия."""
    Category = apps.get_model("catalog", "Category")
    used = set()
    for category in Category.objects.order_by("pk"):
        base = slugify(category.name, allow_unicode=True) or "category"
        slug = base
        suffix = 1
        while slug in used:
            suffix += 1
            slug = f"{base}-{suffix}"
        used.add(slug)
        category.slug = slug
        category.save(update_fields=["slug"])


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_product_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                blank=True,
                default="",
                help_text="Используется в URL; заполняется автоматически из названия",
                max_length=120,
                verbose_name="Слаг",
            ),
            preserve_default=False,
        ),
        migrations.RunPython(fill_slugs, migrations.RunPython.noop),
    ]
