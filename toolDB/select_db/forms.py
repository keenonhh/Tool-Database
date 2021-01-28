from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from toolDB.models import Track


class SearchForm(FlaskForm):
    track_id = IntegerField('track ID', validators=[DataRequired(), NumberRange(min=Track.query.first().id, max=Track.query.order_by(Track.id.desc()).first().id)])
    submit = SubmitField('Search')