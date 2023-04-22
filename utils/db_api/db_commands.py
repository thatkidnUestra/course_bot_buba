from asgiref.sync import sync_to_async

from admin_panel.telebot.models import Users, Games, Adds


@sync_to_async()
def create_user(telegram_id):
    Users.objects.get_or_create(telegram_id=telegram_id)


@sync_to_async()
def get_user(telegram_id):
    return Users.objects.filter(telegram_id=telegram_id).first()


@sync_to_async()
def update_name(telegram_id, name):
    Users.objects.filter(telegram_id=telegram_id).update(name=name)


@sync_to_async()
def get_user_info(telegram_id):
    data = Users.objects.filter(telegram_id=telegram_id).first()

    if data.name is None or data.nickname is None or data.age is None:
        return True
    else:
        return False


@sync_to_async()
def get_user(telegram_id):
    return Users.objects.filter(telegram_id=telegram_id).first()


@sync_to_async()
def get_games():
    return Games.objects.all()


@sync_to_async()
def get_game_by_id(game_id):
    return Games.objects.filter(id=game_id).first()


@sync_to_async()
def create_row_adds(owner_id, name, nickname, age, description, game):
    Adds.objects.get_or_create(
        owner=owner_id,
        name=name,
        nickname=nickname,
        age=age,
        description=description,
        game=game
    )


@sync_to_async()
def get_info_row(owner_id):
    return Adds.objects.filter(owner=owner_id).first()


@sync_to_async()
def update_game(owner_id, game):
    Adds.objects.filter(owner=owner_id).update(game=game)


@sync_to_async()
def update_desc(owner_id, desk):
    Adds.objects.filter(owner=owner_id).update(description=desk)
