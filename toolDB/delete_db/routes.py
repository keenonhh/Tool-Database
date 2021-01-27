from flask import render_template, request, Blueprint, redirect, url_for, flash
from toolDB import db
from toolDB.models import Album, Track, Member, Shows, SetList, trackBandMember

delete = Blueprint('delete', __name__)

## DELETE FUNCTIONALITIES

#deletes an album with the provided album id and returns the album page which displays the album table (minus the deleted album) from the back-end database
@delete.route("/delete_album/<int:id>")
def delete_album(id):
    album = Album.query.filter_by(id=id).first()
    db.session.delete(album)
    db.session.commit()
    rows = Album.query.all()
    return render_template('album.html', title='Album', header='Album Table', rows=rows)

#deletes a band member with the provided band member id and returns the band member page which displays the band members table (minus the deleted band member) from the back-end database
@delete.route("/delete_member/<int:id>")
def delete_member(id):
    member = Member.query.filter_by(id=id).first()
    db.session.delete(member)
    db.session.commit()
    rows = Member.query.all()
    return render_template('member.html', title='Member', header='Member Table', rows=rows)
    
#deletes a show with the provided line up id and returns the shows page which displays the shows table (minus the deleted show) from the back-end database    
@delete.route("/delete_show/<int:id>")
def delete_show(id):
    show = Shows.query.filter_by(id=id).first()
    db.session.delete(show)
    db.session.commit()
    rows = Shows.query.all()
    return render_template('shows.html', title='Shows', header='Shows Table', rows=rows)   

#deletes a track with the provided track id and returns the track page which displays the tracks table (minus the deleted track) from the back-end database    
@delete.route("/delete_track/<int:id>")
def delete_track(id):
    track = Track.query.filter_by(id=id).first()
    db.session.delete(track)
    db.session.commit()
    rows = Track.query.all()
    return render_template('track.html', title='Track', header='Track Table', rows=rows) 

#deletes a track contributor with the provided track band contributor id and returns the track contributors page which displays the track band members table (minus the deleted track contributor) from the back-end database    
@delete.route("/delete_contributor/<int:id>")
def delete_contributor(id):
    # since trackBandMember is an assocaiteive table the two tables it is assocaiting must be joined
    # to return the raow associated with the id
    contributor = Track.query.join(trackBandMember).join(Member).filter(trackBandMember.c.id==id).first()
    db.session.delete(contributor)
    db.session.commit()
    rows = db.session.execute('SELECT trackBandMember.id, trackBandMember.track_id, track.track_name, trackBandMember.member_id, member.member_name FROM trackBandMember JOIN track ON trackBandMember.track_id = track.id JOIN member ON trackBandMember.member_id = member.id;')
    return render_template('track_contributors.html', title='Track Contributors', header='Track Contributors', rows=rows)
     
#deletes a set list with the provided set list id and returns the set list page which displays the set list table (minus the deleted set list) from the back-end database        
@delete.route("/delete_set_list/<int:id>")
def delete_set_list(id):
    set_list = SetList.query.filter_by(id=id).first()
    db.session.delete(set_list)
    db.session.commit()
    rows = db.session.query(SetList, Track, Shows).filter(SetList.id == SetList.id).filter(SetList.show_id == Shows.id).filter(SetList.track_id == Track.id).all()
    return render_template('set_list.html', title='Set List', header='Set List Table', rows=rows) 

