from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    body = StringField('Žinutė', validators=[DataRequired()])
    submit = SubmitField('Siųsti')


class SeenPostForm(PostForm):
    seen = BooleanField('Perskaityta')
