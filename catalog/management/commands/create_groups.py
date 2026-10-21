from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

MODERATOR_GROUP_NAME = "Модератор продуктов"


class Command(BaseCommand):
    help = "Создаёт группы с правами для модераторов"

    def handle(self, *args, **options):
        moderator_group, _ = Group.objects.get_or_create(name=MODERATOR_GROUP_NAME)

        permissions = Permission.objects.filter(
            codename__in=[
                "can_unpublish_product",
                "delete_product",
            ]
        )

        moderator_group.permissions.set(permissions)

        self.stdout.write(
            self.style.SUCCESS(
                f"Группа «{MODERATOR_GROUP_NAME}» создана. "
                f"Права: {list(permissions.values_list('codename', flat=True))}"
            )
        )