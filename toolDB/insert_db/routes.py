from flask import render_template, request, Blueprint, redirect, url_for, flash
from toolDB.insert_db.forms import AddAlbumForm, AddTrackForm, AddTrackForm, AddShowForm
from toolDB import db
from toolDB.models import Album, Track, Member, Shows, SetList, trackBandMember

insert = Blueprint('insert', __name__)

### INSERT FUNCTIONALITIES

#renders the add album page which allows user to enter details about a new album
@insert.route('/add_album', methods=['GET','POST'])
def add_album():
    form = AddAlbumForm()
    if form.validate_on_submit():
        album = Album(album_name=form.album_name.data, release_date=form.release_date.data)
        # add the user to database
        db.session.add(album)
        db.session.commit()
        # success message 
        flash(f'Album has been added!', 'success')
        # redirect to lifts page 
        return redirect(url_for('select.album'))
    return render_template('add_album.html', title='Add Album', header='Add Album', form=form)

#renders the add track page which allows user to enter details about a new track
@insert.route('/add_track', methods=['GET','POST'])
def add_track():
    form = AddTrackForm()
    if form.validate_on_submit():
        track = Track(track_name=form.track_name.data, track_length=form.track_length.data, album_id=form.album_id.data)
        # add the user to database
        db.session.add(track)
        db.session.commit()
        # success message 
        flash(f'Track has been added!', 'success')
        flash(f"Don't forget to add the track's contributing band member(s) under Track Contributors!", 'message')
        # redirect to lifts page 
        return redirect(url_for('select.track'))
    return render_template('add_track.html', title='Add Track', header='Add track', form=form)  
     
#renders the add band member page which allows user to enter details about a new band member   
@insert.route('/add_band_members', methods=['GET','POST'])
def add_band_members():
    form = AddTrackForm()
    if form.validate_on_submit():
        member = Member(member_name=form.member_name.data, instrument=form.instrument.data, birthdate=form.birthdate.data)
        # add the user to database
        db.session.add(member)
        db.session.commit()
        # success message 
        flash(f'Member has been added!', 'success')
        # redirect to lifts page 
        return redirect(url_for('select.band_members'))
    return render_template('add_members.html', title='Add Member', header='Add Member', form=form) 

#renders the add show page which allows user to enter details about a new show
@insert.route('/add_shows', methods=['GET','POST'])
def add_shows():
    form = AddShowForm()
    if form.validate_on_submit():
        show = Shows(city=form.city.data, set_list_id=form.set_list_id.data)
        # add the user to database
        db.session.add(show)
        db.session.commit()
        # success message 
        flash(f'Show has been added!', 'success')
        # redirect to lifts page 
        return redirect(url_for('select.shows'))
    return render_template('add_shows.html', title='Add Shows', header='Add Shows', form=form)
  

##renders the add set list page which allows user to enter details about a new set list
#@insert.route('/add_set_list', methods=['GET','POST'])
#def add_set_list():
#    db_connection = connect_to_database()
#    query1 = 'SELECT `line up id`, `city` FROM `shows`';
#    query2 = 'SELECT `track id`, `track name` FROM `tracks`';
#    result_lineup = execute_query(db_connection, query1).fetchall();
#    result_track = execute_query(db_connection, query2).fetchall();
#    return render_template('add_set_list.html', lineup_id = result_lineup, track_id = result_track)
#
  
##renders the add track contributor page which allows user to enter details about a new track contributor
#@insert.route('/add_track_contributors', methods=['GET','POST'])
#def add_track_contributors():
#    db_connection = connect_to_database()
#    query1 = 'SELECT `band member id`, `name` FROM `band members`';
#    query2 = 'SELECT `track id`, `track name` FROM `tracks`';
#    result_bm = execute_query(db_connection, query1).fetchall();
#    result_track = execute_query(db_connection, query2).fetchall();
#    return render_template('add_track_contributors.html', members_name = result_bm, track_name = result_track)   
#
  