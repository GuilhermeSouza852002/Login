from flask_login import LoginManager

from model import Personagem

login_manager = LoginManager()


@login_manager.user_loader
def personagem_loader(personagem_id):
    return Personagem.query.get(personagem_id)
