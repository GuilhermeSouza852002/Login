from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, DateField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Logar")


class RegisterForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    classe = StringField("Classe", validators=[DataRequired()])
    hp = StringField("Vida-Max", validators=[DataRequired()])
    lv = StringField("Level", validators=[DataRequired()])
    forca = StringField("Força", validators=[DataRequired()])
    destreza = StringField("Destreza", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[
        DataRequired(),
        EqualTo("confirm", message="Senhas devem ser compatíveis")])
    confirm = PasswordField("Confirmação")
    birthdate = DateField("Data de aniversário", validators=[DataRequired()], format=["%d/%m/%Y", "%Y-%m-%d"])
    submit = SubmitField("Cadastrar")
