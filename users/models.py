from tabnanny import verbose

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to="users/avatars/",
        null=True,
        blank=True,
        verbose_name="Аватар",
        help_text='Загрузите свой аватар'
    )
    phone = models.CharField(max_length=35, verbose_name="Телефон", blannk=True, null=True,
                             help_text='Введите номер телефона')
    country = models.CharField(max_length=100, verbose_name="Страна",  blannk=True, null=True, help_text='Введите страну')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_mame = "Пользователь"
        verbose_name_plural = "Пользователи"

        def __str__(self):
            return self.email

