from django.apps import AppConfig


class CatalogConfig(AppConfig):
    name = "catalog"

    def ready(self):
        # Подключаем сигналы сброса кеша
        from catalog import signals  # noqa: F401
