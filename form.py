from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class PiperackArea(FlaskForm):
    ancho = IntegerField('Ancho', validators=[DataRequired()])
    alto = IntegerField('Alto',validators=[DataRequired()])
    submit = SubmitField('Enter')


class Equipos(FlaskForm):
    nombreEquipo = StringField('Nombre del Equipo', validators=[DataRequired()])
    tag = StringField('TAG',validators=[DataRequired()])
    coorX =IntegerField('Coordenada en X',validators=[DataRequired()])
    coorY =IntegerField('Coordenada en Y',validators=[DataRequired()])
    coorZ =IntegerField('Coordenada en Z',validators=[DataRequired()])
    tipoEquipo = StringField('Tipo de equipo',validators=[DataRequired()])
    submit = SubmitField('Enter')