# Flask Foundation

Three different levels in each branch

## Basic
* Create a virtual enviornment
    * virtualenv env
    * source env/bin/activate
* install flask inside of the virtual env
    * pip install flask
* Two different ways to run this flask app
    * One
        * In terminal:
            export FLASK_APP=app.py
            export FLASK_DEBUG=development
            flask run
    * Two
        * Include in the python file:
            if __name__ == '__main__'
                app.run(debug=True, port=3000)
        * python app.py

## Database
* Using postgres with psycopg2
    * create a database
        * In Terminal: createdb todoapp
    * pip install psycopg2

* Using postgres with SQLAlchemy
    * install flask_sqlalchemy AND psycopg2 

## Migration

## Advanced
* using the flaskr folder structure