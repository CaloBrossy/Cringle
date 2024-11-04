from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
import sqlalchemy as sa
from app import db
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(('Nombre de usuario'), validators=[DataRequired()])
    about_me = TextAreaField(('Sobre mi'), validators=[Length(min=0, max=140)])
    submit = SubmitField(('¡Listo!'))

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(
                User.username == username.data))
            if user is not None:
                raise ValidationError(('Use un nombre diferente.'))


class EmptyForm(FlaskForm):
    submit = SubmitField('¡Listo!')


class PostForm(FlaskForm):
    post = TextAreaField(('Di algo..'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(('¡Listo!'))

class MessageForm(FlaskForm):
    message = TextAreaField(('Mensaje'), validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField(('Enviar'))
