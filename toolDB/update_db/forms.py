from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField, SelectField, DateField
from wtforms.validators import DataRequired, Length, NumberRange
from toolDB.models import Album, Track, Member, Shows, Setlist, trackbandmember


# Form to add an album to database
class UpdateAlbumForm(FlaskForm):
    album_name = StringField('Album Name', validators=[DataRequired(), Length(min=2, max=20)])
    release_date = DateField('Release Date', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Update Album')

class UpdateTrackForm(FlaskForm):
    track_name = StringField('Track Name', validators=[DataRequired(), Length(min=2, max=20)])
    track_length = FloatField('Track Length', validators=[DataRequired()])
    # Validate that the track album_id is within the range of album album_ids
    album_id = IntegerField('Album ID', validators=[DataRequired(), NumberRange(min=Album.query.first().id, max=Album.query.order_by(Album.id.desc()).first().id)])
    submit = SubmitField('Update Track')

class UpdateMemberForm(FlaskForm):
    member_name = StringField('Member Name', validators=[DataRequired(), Length(min=2, max=20)])
    instrument = StringField('Instrument', validators=[DataRequired(), Length(min=2, max=20)])
    birthdate = DateField('Birthdate', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Update Member')

class UpdateShowForm(FlaskForm):
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Update Show')

class UpdateSetlistForm(FlaskForm):
    track_name = SelectField('Track Name', validators=[DataRequired()])
    submit = SubmitField('Update Set List')


