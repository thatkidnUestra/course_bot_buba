from asgiref.sync import sync_to_async

from admin_panel.telebot.models import Users


@sync_to_async()
def create_user(telegram_id):
    Users.objects.get_or_create(telegram_id=telegram_id)


@sync_to_async()
def get_user(telegram_id):
    return Users.objects.filter(telegram_id=telegram_id).first()


@sync_to_async()
def update_name(telegram_id, name):
    Users.objects.filter(telegram_id=telegram_id).update(name=name)
