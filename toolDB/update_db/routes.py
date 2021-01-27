from flask import render_template, request, Blueprint, redirect, url_for, flash
from toolDB.update_db.forms import UpdateAlbumForm, UpdateTrackForm, UpdateMemberForm, UpdateShowForm, UpdateSetListForm
from toolDB import db
from toolDB.models import Album, Track, Member, Shows, SetList

update = Blueprint('update', __name__)


### UPDATE FUNCTIONALITIES        

#update tracks table
@update.route('/update_track/<int:id>', methods=['POST','GET'])
def update_tracks(id):
    form = UpdateTrackForm()
    # display the selected row on the update page
    row = Track.query.filter_by(id=id).first()
 
    if form.validate_on_submit():
        # update the selected row with the values from the form
        Track.query.filter_by(id=id).update({'track_name':form.track_name.data, 'track_length':form.track_length.data, 'album_id':form.album_id.data})
        db.session.commit()
        # success message 
        flash(f'Track has been updated!', 'success')
        # redirect to track page 
        return redirect(url_for('select.track'))
    return render_template('track_update.html', title='Update Track', header='Update Track Table', form=form, row=row)

#update set list table
@update.route('/update_set_list/<int:id>', methods=['POST','GET'])
def update_set_list(id):
    form = UpdateSetListForm()
    # display the selected row on the update page
    row = db.session.query(SetList, Track, Shows).filter(SetList.id==id).filter(SetList.show_id == Shows.id).filter(SetList.track_id == Track.id).first()
    
    # choices for form drop down
    form.track_name.choices = [(track.id, track.track_name) for track in Track.query.order_by('track_name')]

    # submit the update form
    if form.validate_on_submit():
        # update the selected row with the values from the form
        SetList.query.filter_by(id=id).update({'track_id':form.track_name.data})
        db.session.commit()
        # success message 
        flash(f'Set List has been updated!', 'success')
        # redirect to set list page 
        return redirect(url_for('select.set_list'))
    return render_template('set_list_update.html', title='Update Set List', header='Update Set List Table', form=form, row=row)


#update shows table
@update.route('/update_show/<int:id>', methods=['POST','GET'])
def update_show(id):
    form = UpdateShowForm()
    # display the selected row on the update page
    row = Shows.query.filter_by(id=id).first()
 
    # submit the update form
    if form.validate_on_submit():
        # update the selected row with the values from the form
        Shows.query.filter_by(id=id).update({'city':form.city.data})
        db.session.commit()
        # success message 
        flash(f'Show updated!', 'success')
        # redirect to shows page 
        return redirect(url_for('select.shows'))
    return render_template('shows_update.html', title='Update Show', header='Update Show Table', form=form, row=row)
        
#update album table        
@update.route('/update_album/<int:id>', methods=['POST','GET'])
def update_album(id):
    form = UpdateAlbumForm()
    # display the selected row on the update page
    row = Album.query.filter_by(id=id).first()
 
    # submit the update form
    if form.validate_on_submit():
        # update the selected row with the values from the form
        Album.query.filter_by(id=id).update({'album_name':form.album_name.data, 'release_date':form.release_date.data})
        db.session.commit()
        # success message 
        flash(f'Album updated!', 'success')
        # redirect to album page 
        return redirect(url_for('select.album'))
    return render_template('album_update.html', title='Update Album', header='Update Album Table', form=form, row=row)
      
#update band members table    
@update.route('/update_member/<int:id>', methods=['POST','GET'])
def update_member(id):
    form = UpdateMemberForm()
    # display the selected row on the update page
    row = Member.query.filter_by(id=id).first()
 
    # submit the update form
    if form.validate_on_submit():
        # update the selected row with the values from the form
        Member.query.filter_by(id=id).update({'member_name':form.member_name.data, 'instrument':form.instrument.data, 'birthdate':form.birthdate.data})
        db.session.commit()
        # success message 
        flash(f'Member updated!', 'success')
        # redirect to album page 
        return redirect(url_for('select.band_members'))
    return render_template('members_update.html', title='Update Member', header='Update Member Table', form=form, row=row)
