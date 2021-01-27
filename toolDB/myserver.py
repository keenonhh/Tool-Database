
### SEARCH FUNCTION
# 
##returns the results of the user's search by track id - information is displayed about the specified track from the tracks, shows, and band members tables 
#@app.route("/search", methods = ['GET', 'POST'])
#def search():
#    db_connection = connect_to_database()
#    track_id = request.form['Search']
#    query = 'SELECT `tracks`.`track id`, `tracks`.`track name`, `tracks`.`track length`, `tracks`.`album id`, `band members`.`name`, `shows`.`line up id`, `shows`.`city` FROM `tracks` LEFT JOIN `set list` ON `tracks`.`track id` = `set list`.`track id` LEFT JOIN `shows` ON `set list`.`line up id` = `shows`.`line up id` LEFT JOIN `track band member` ON `tracks`.`track id` = `track band member`.`track id` LEFT JOIN `band members` ON `track band member`.`band member id` = `band members`.`band member id` WHERE `tracks`.`track id` = (%s)'
#    data = (track_id,)
#    result_search = execute_query(db_connection, query, data).fetchall();
#    return render_template('results.html', results = result_search)    
# 
