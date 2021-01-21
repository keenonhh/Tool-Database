import MySQLdb as mariadb
from db_credentials import host, user, passwd, db

#connects to a database and returns a database object
def connect_to_database(host = host, user = user, passwd = passwd, db = db):
    db_connection = mariadb.connect(host,user,passwd,db)
    return db_connection


#executes a given SQL query on the given db connection and returns a Cursor object
def execute_query(db_connection = None, query = None, query_params = ()):
    if db_connection is None:
        print("No connection to the database found!")
        return None

    if query is None or len(query.strip()) == 0:
        print("Query is empty! Please pass a SQL query in query")
        return None

    print("Executing %s with %s" % (query, query_params));
    # Create a cursor to execute query
    cursor = db_connection.cursor()

    '''
    params = tuple()
    #create a tuple of parameters to send with the query
    for q in query_params:
        params = params + (q)
    '''
    cursor.execute(query, query_params)
    
    #commit any changes to the database
    db_connection.commit();
    return cursor