from flask import render_template, request, Blueprint
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
    return render_template('album.html', title='Album', table_name='Album Table', rows=rows)

#renders the track page and displays the tracks table from the back-end database
@select.route('/track')
def track():
    rows = Track.query.all()  
    return render_template('track.html', title='Track', table_name='Track Table', rows=rows)

#renders the band members page and displays the band members table from the back-end database
@select.route('/band_members')
def band_members():
    rows = Member.query.all()  
    return render_template('member.html', title='Band Members', table_name='Band Members', rows=rows)

#renders the shows page and displays the shows table from the back-end database
@select.route('/shows')
def shows():
    rows = Shows.query.all()  
    return render_template('shows.html', title='Shows', table_name='Shows', rows=rows)

### need to perform joins to get track name and city name 
#renders the set list page and displays the set list table, along with the corresponding columns from the shows and tracks table, from the back-end database
@select.route('/set_list')
def set_list():
    rows = SetList.query.all()  
    return render_template('set_list.html', title='SetList', table_name='Set List table', rows=rows)



## need to perform joins to get member names/IDs
#renders the track contributors page and displays the track band members table, along with the corresponding columns from the tracks and band members tables, from the back-end database 
@select.route('/track_contributors')
def track_contributors():
    rows = Track.query.join(trackBandMember).join(Member).filter((trackBandMember.c.track_id == Track.id) & (trackBandMember.c.member_id == Member.id)).all()
    return render_template('track_contributors.html', title='Track Contributors', table_name='Track Contributors', rows=rows)