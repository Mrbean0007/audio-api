# audio-api

## Install pipenv 
`pip install pipenv`

Install the dependences from pipfile

`pipenv install`

## Add database

1. Create .env file in same directory
2. SECRET_KEY = 'sqlite:////tmp/test.db' 
3. For my MySql/Postgress ='dialect+driver://username:password@host:port/database'
  
  [Refernce for database] (https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#configuration-keys)

## Create Models in database

1.Enter your python shell using  `python` or `python3` in command prompt inside the same directory
2. Import the file

``` python
from audio import db
db.create_all()

``` 
## Run the app.py for generic response base or app2.py for generic route base

`python app.py`
