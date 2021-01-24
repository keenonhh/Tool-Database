from flask_sqlalchemy import SQLAlchemy
from toolDB import db


# Table of Tool albums
class Album(db.Model):
    # primary key of table  
    id = db.Column(db.Integer, primary_key=True)

    # album info
    album_name = db.Column(db.String, nullable=False)
    release_date = db.Column(db.String, nullable=False)
    
    # there is a relationship which is album contains many tracks
    # and tracks come from a single album (many to one)
    track = db.relationship('Track', backref='album', lazy=True)

    # relationship between setlist and album
    # Each setlist is from one album (one to one(or none))
    set_list_album = db.relationship('SetList', backref='album', lazy=True)

    # display the album info
    def __repr__(self):
        return f"album('{self.album_name}', '{self.release_date}')"

# Table of Tool tracks
class Track(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)

    # track info
    track_name = db.Column(db.String, nullable=False)
    track_length = db.Column(db.Float, nullable=False)

    # album id is a foreign key column in this table indicating which tracks
    # are on which album
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

    # there is a relationship which band member(s) wrote which tracks (many to many)
    member_track = db.relationship('Member', secondary='trackBandMember', backref='track', lazy=True)

    # relationship between setlist and track
    set_list_track = db.relationship('SetList', backref='track', lazy=True)

    def __repr__(self):
        return f"track('{self.track_name}', '{self.track_length}')"

# Table of Tool members
class Member(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)

    # band member info
    member_name = db.Column(db.String, nullable=False)
    instrument = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.String, nullable=False)
   
    def __repr__(self):
        return f"member('{self.member_name}', '{self.instrument}', {self.birthdate})"

# associative table between tracks and members that represents 
# the many to many relationship
trackBandMember = db.Table('trackBandMember',
    db.Column('track_id', db.Integer, db.ForeignKey('track.id')),
    db.Column('member_id', db.Integer, db.ForeignKey('member.id'))
)

# Table of Tool shows
class Shows(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)

    # track info
    city = db.Column(db.String, nullable=False)
    set_list_id = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"show('{self.city}', '{self.set_list_id}')"

# Table of Tool shows
class SetList(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)

    set_list_id = db.Column(db.Integer, nullable=False)

    # setlist info
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), nullable=False)

    def __repr__(self):
        return f"setlist('{self.album_id}', '{self.track_id}')"