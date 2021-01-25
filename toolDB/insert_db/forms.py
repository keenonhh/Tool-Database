from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange
from toolDB.models import Album, Track, Member, Shows, SetList, trackBandMember

# Form to add an album to database
class AddAlbumForm(FlaskForm):
    album_name = StringField('Album Name', validators=[DataRequired(), Length(min=2, max=20)])
    release_date = StringField('Release Date', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add Album')

class AddTrackForm(FlaskForm):
    track_name = StringField('Track Name', validators=[DataRequired(), Length(min=2, max=20)])
    track_length = FloatField('Track Length', validators=[DataRequired()])
    # Validate that the track album_id is within the range of album album_ids
    album_id = IntegerField('Album ID', validators=[DataRequired(), NumberRange(min=Album.query.first().id, max=Album.query.order_by(Album.id.desc()).first().id)])
    submit = SubmitField('Add Track')


class AddTrackForm(FlaskForm):
    member_name = StringField('Member Name', validators=[DataRequired(), Length(min=2, max=20)])
    instrument = StringField('Instrument', validators=[DataRequired(), Length(min=2, max=20)])
    birthdate = StringField('Birthdate', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add Member')

class AddShowForm(FlaskForm):
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])
    set_list_id = IntegerField('Set List ID', validators=[DataRequired()])
    submit = SubmitField('Add Show')