from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class second_game_const_form(FlaskForm):
    text = StringField(validators = [DataRequired()])
