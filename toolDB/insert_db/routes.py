from flask import render_template, request, Blueprint, redirect, url_for, flash
from toolDB.insert_db.forms import AddAlbumForm, AddTrackForm, AddMemberForm, AddShowForm, AddSetListForm, AddTrackContributorForm
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
        # add the album to database
        db.session.add(album)
        db.session.commit()
        # success message 
        flash(f'Album has been added!', 'success')
        # redirect to album page 
        return redirect(url_for('select.album'))
    return render_template('add_album.html', title='Add Album', header='Add Album', form=form)

#renders the add track page which allows user to enter details about a new track
@insert.route('/add_track', methods=['GET','POST'])
def add_track():
    form = AddTrackForm()
    if form.validate_on_submit():
        track = Track(track_name=form.track_name.data, track_length=form.track_length.data, album_id=form.album_id.data)
        # add the track to database
        db.session.add(track)
        db.session.commit()
        # success message 
        flash(f'Track has been added!', 'success')
        flash(f"Don't forget to add the track's contributing band member(s) under Track Contributors!", 'message')
        # redirect to track page 
        return redirect(url_for('select.track'))
    return render_template('add_track.html', title='Add Track', header='Add track', form=form)  
     
#renders the add band member page which allows user to enter details about a new band member   
@insert.route('/add_band_members', methods=['GET','POST'])
def add_band_members():
    form = AddMemberForm()
    if form.validate_on_submit():
        member = Member(member_name=form.member_name.data, instrument=form.instrument.data, birthdate=form.birthdate.data)
        # add the member to database
        db.session.add(member)
        db.session.commit()
        # success message 
        flash(f'Member has been added!', 'success')
        # redirect to members page 
        return redirect(url_for('select.band_members'))
    return render_template('add_members.html', title='Add Member', header='Add Member', form=form) 

#renders the add show page which allows user to enter details about a new show
@insert.route('/add_shows', methods=['GET','POST'])
def add_shows():
    form = AddShowForm()
    if form.validate_on_submit():
        show = Shows(city=form.city.data)
        # add the show to database
        db.session.add(show)
        db.session.commit()
        # success message 
        flash(f'Show has been added!', 'success')
        # redirect to shows page 
        return redirect(url_for('select.shows'))
    return render_template('add_shows.html', title='Add Shows', header='Add Shows', form=form)
  

#renders the add set list page which allows user to enter details about a new set list
@insert.route('/add_set_list', methods=['GET','POST'])
def add_set_list():
    form = AddSetListForm()
    
    # populate the list of choices with the cities and tracks availalbe
    form.show_id.choices = [(show.id, show.city) for show in Shows.query.order_by('city')]
    form.track_name.choices = [(track.id, track.track_name) for track in Track.query.order_by('track_name')]

    if form.validate_on_submit():
        # use the track id to get the album id so a new setlist can be added
        set_list = SetList(show_id=form.show_id.data, track_id=form.track_name.data)
        # add the set list to database
        db.session.add(set_list)
        db.session.commit()
        # success message 
        flash(f'Set list has been added!', 'success')
        # redirect to set list page 
        return redirect(url_for('select.set_list'))
    return render_template('add_set_list.html', title='Add to a Setlist', header='Add to a Setlist', form=form)

  
#renders the add track contributor page which allows user to enter details about a new track contributor
@insert.route('/add_track_contributors', methods=['GET','POST'])
def add_track_contributors():
    form = AddTrackContributorForm()

    # populate the list of choices with the track names and member names
    form.track_name.choices = [(track.id, track.track_name) for track in Track.query.order_by('track_name')]
    form.member.choices = [(mem.id, mem.member_name) for mem in Member.query.order_by('member_name')]

    if form.validate_on_submit():
        # statement that will insert into many to many associative table
        # track_id and member_name from form will be inserted upon execution and commit
        track_contributor = trackBandMember.insert().values(track_id=form.track_name.data, member_id=form.member.data)
        # add the track contributor to database
        db.session.execute(track_contributor)
        db.session.commit()
        # success message 
        flash(f'Track Contributor has been added!', 'success')
        # redirect to track contributors page 
        return redirect(url_for('select.track_contributors'))
    return render_template('add_track_contributors.html', title='Add Track Contributor', header='Add Track Contributor', form=form)

  