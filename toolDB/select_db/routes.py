from flask import render_template, Blueprint
from toolDB import db
from toolDB.models import Album, Track, Member, Shows, SetList, trackBandMember

select = Blueprint('select', __name__)

## SELECT FUNCTIONALITIES

#renders the home page
@select.route('/')
def index():
    return render_template('index.html', title='Home')

#renders the album page and displays the album table from the back-end database
@select.route('/album')
def album():
    rows = Album.query.all()  
    return render_template('album.html', title='Album', header='Album Table', rows=rows)

#renders the track page and displays the tracks table from the back-end database
@select.route('/track')
def track():
    rows = Track.query.all()  
    return render_template('track.html', title='Track', header='Track Table', rows=rows)

#renders the band members page and displays the band members table from the back-end database
@select.route('/band_members')
def band_members():
    rows = Member.query.all()  
    return render_template('member.html', title='Band Members', header='Band Members', rows=rows)

#renders the shows page and displays the shows table from the back-end database
@select.route('/shows')
def shows():
    rows = Shows.query.all()  
    return render_template('shows.html', title='Shows', header='Shows', rows=rows)
 
#renders the set list page and displays the set list table, along with the corresponding columns from the shows and tracks table, from the back-end database
@select.route('/set_list')
def set_list():
    rows = db.session.execute('SELECT set_list.id, set_list.show_id, shows.city, set_list.track_id, track.track_name FROM set_list JOIN shows ON set_list.show_id = shows.id JOIN track ON set_list.track_id = track.id;')
    return render_template('set_list.html', title='SetList', header='Set List table', rows=rows)

#renders the track contributors page and displays the track band members table, along with the corresponding columns from the tracks and band members tables, from the back-end database 
@select.route('/track_contributors')
def track_contributors():
    rows = db.session.execute('SELECT trackBandMember.id, trackBandMember.track_id, track.track_name, trackBandMember.member_id, member.member_name FROM trackBandMember JOIN track ON trackBandMember.track_id = track.id JOIN member ON trackBandMember.member_id = member.id;')
    return render_template('track_contributors.html', title='Track Contributors', header='Track Contributors', rows=rows)