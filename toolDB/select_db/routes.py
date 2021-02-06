from flask import render_template, Blueprint, redirect, url_for
from toolDB import db
from toolDB.select_db.forms import SearchForm
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
@select.route('/track', methods = ['GET', 'POST'])
def track():
    # form for the search field
    form = SearchForm()
    rows = Track.query.all()
    # if a valid search is performed send the track id that was searched for to the search function
    if form.validate_on_submit():
        id = form.track_id.data
        # redirect to search page 
        return redirect(url_for('select.search', id=id))
    return render_template('track.html', title='Track', header='Track Table', rows=rows, form=form)

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
    rows = db.session.query(SetList, Track, Shows).filter(SetList.id == SetList.id).filter(SetList.show_id == Shows.id).filter(SetList.track_id == Track.id).all()
    return render_template('set_list.html', title='SetList', header='Set List table', rows=rows)

#renders the track contributors page and displays the track band members table, along with the corresponding columns from the tracks and band members tables, from the back-end database 
@select.route('/track_contributors')
def track_contributors():
    rows = db.session.query(Track, Member).filter(Member.id == trackBandMember.c.member_id).filter(Track.id == trackBandMember.c.track_id).all()
    return render_template('track_contributors.html', title='Track Contributors', header='Track Contributors', rows=rows)

# Search functionality is essentially just selecting from the database
@select.route("/search/<int:id>", methods = ['GET', 'POST'])
def search(id):
    rows = db.session.query(Track, Member, Shows, SetList).filter(Track.id == id).filter(trackBandMember.c.track_id == Track.id).filter(Member.id == trackBandMember.c.id).filter(SetList.track_id == id).filter(Shows.id == SetList.show_id).all()   
    return render_template('results.html', title='Search Results', header='Search Results', rows=rows)