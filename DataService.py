
def getData():
    import sqlite3
    # Create a connection to the SQLite database
    conn = sqlite3.connect('pocdb.db')

    # Create a cursor object
    cur = conn.cursor()
    # Execute a query
    cur.execute("SELECT * FROM Employee")



    # Fetch all the rows
    rows = cur.fetchall()

    #for row in rows:
        #print(row)

    # Get the column names from the cursor description
    columns = [desc[0] for desc in cur.description]
    return rows,columns

  
