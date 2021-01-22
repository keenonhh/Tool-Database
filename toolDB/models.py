from flask_sqlalchemy import SQLAlchemy
from toolDB import db


# Table of Tool albums
class Album(db.Model):
    # primary key of table
    id = db.Column(db.Integer, primary_key=True)

    # album info
    album_name = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    
    track = db.relationship('Track', backref='album', lazy=True)

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

    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
   
    
    def __repr__(self):
        return f"track('{self.track_name}', '{self.track_length}')"