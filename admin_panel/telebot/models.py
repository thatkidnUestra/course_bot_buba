from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Users(models.Model):
    telegram_id = models.BigIntegerField()  # Поле с Telegram ID пользователя, которое может быть огромным числом

    name = models.CharField(
        null=True,
        max_length=30
    )

    nickname = models.CharField(
        null=True,
        max_length=30
    )

    age = models.IntegerField(
        null=True
    )
