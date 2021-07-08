from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Create the connections. You can also add a user like this: psycopg2.connect('dbname=todoapp user=anthony')
conn = psycopg2.connect('dbname=todoapp')

# Open a cursor to perform database operations
#   After connecting, we're working within a **session** 
#   and you can start **committing** these **transactions** 
#       (which are units of work, remember) to start interacting with our database
cursor = conn.cursor() #call cursor "cur"

# Drop any existing todo tables
cursor.execute("DROP TABLE IF EXISTS todos;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cursor.execute("""
    CREATE TABLE todos (
        id BIGSERIAL PRIMARY KEY,
        description VARCHAR NOT NULL
    );
""")

cursor.execute("INSERT INTO todos (description) VALUES ('Go to gym');")
cursor.execute("INSERT INTO todos (description) VALUES ('Go to picnic');")
cursor.execute("INSERT INTO todos (description) VALUES ('Go to the factory');")

# Commit, so it does the executions on the database and persists in the database
conn.commit()

# We can say this is all the work we want to do in this session by calling close on the connection and the cursor 
# psycopg2 will NOT automatically close out a session for you, so this is something you'll have to do manually every time you start a session
cursor.close()
conn.close()

#You can check psql to see if it worked 
# In terminal:
#   * psql todoapp #this opens the todoapp inside of psql. If you just wanted to open psql, just write: psql
#   * \dt

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        conn = psycopg2.connect('dbname=todoapp')
        cursor = conn.cursor()
        
        data = request.form['item']
        cursor.execute("INSERT INTO todos (description) VALUES (%s)", (data,)) #psycopg2 uses the %s to sanitize and user inputs, so they can't cause harm. It takes a tuple after the string.

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))
    else: #This is for GET methods
        conn = psycopg2.connect('dbname=todoapp')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM todos;')
        items = cursor.fetchall()
        
        conn.commit()
        cursor.close()
        conn.close()

        return render_template('index.html', items=items)



if __name__ == '__main__':
    app.run(port=3000, debug=True)