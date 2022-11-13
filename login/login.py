from flask_login import LoginManager

from model import Personagem

login_manager = LoginManager()


@login_manager.user_loader
def user_loader(user_id):
    return Personagem.query.get(user_id)
