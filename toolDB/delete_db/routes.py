from flask import render_template, request, Blueprint, redirect, url_for, flash
from toolDB import db
from toolDB.models import Album, Track, Member, Shows, Setlist, trackbandmember

delete = Blueprint('delete', __name__)

## DELETE FUNCTIONALITIES

#deletes an album with the provided album id and returns the album page which displays the album table (minus the deleted album) from the back-end database
@delete.route("/delete_album/<int:id>")
def delete_album(id):
    album = Album.query.filter_by(id=id).first()
    db.session.delete(album)
    db.session.commit()
    return redirect(url_for('select.album'))

#deletes a band member with the provided band member id and returns the band member page which displays the band members table (minus the deleted band member) from the back-end database
@delete.route("/delete_member/<int:id>")
def delete_member(id):
    member = Member.query.filter_by(id=id).first()
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('select.band_members'))   

#deletes a show with the provided line up id and returns the shows page which displays the shows table (minus the deleted show) from the back-end database    
@delete.route("/delete_show/<int:id>")
def delete_show(id):
    show = Shows.query.filter_by(id=id).first()
    db.session.delete(show)
    db.session.commit()
    return redirect(url_for('select.shows'))  

#deletes a track with the provided track id and returns the track page which displays the tracks table (minus the deleted track) from the back-end database    
@delete.route("/delete_track/<int:id>")
def delete_track(id):
    track = Track.query.filter_by(id=id).first()
    db.session.delete(track)
    db.session.commit()
    return redirect(url_for('select.track'))

#deletes a track contributor with the provided track band contributor id and returns the track contributors page which displays the track band members table (minus the deleted track contributor) from the back-end database    
@delete.route("/delete_contributor/<int:mem_id>/<int:track_id>")
def delete_contributor(mem_id, track_id):
    # since trackbandmember is an assocaiteive table the two tables it is associating must be joined
    # to return the row associated with the id
    mem = Member.query.get(mem_id)
    track = Track.query.get(track_id)
    mem.track.remove(track) 
    db.session.commit()
    return redirect(url_for('select.track_contributors'))
    
#deletes a set list with the provided set list id and returns the set list page which displays the set list table (minus the deleted set list) from the back-end database        
@delete.route("/delete_set_list/<int:id>")
def delete_set_list(id):
    set_list = Setlist.query.filter_by(id=id).first()
    db.session.delete(set_list)
    db.session.commit()
    return redirect(url_for('select.set_list'))
