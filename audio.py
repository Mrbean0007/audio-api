from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
database = os.environ['SECRET_KEY']
app = Flask(__name__)
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Product Class/Model


class song(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Name_of_the_song = db.Column(db.String(100), nullable=False)
    Duration_in_number_of_seconds = db.Column(db.Float, nullable=False)
    Updated_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, Name_of_the_song, Duration_in_number_of_seconds, Updated_time):
        self.Name_of_the_song = Name_of_the_song
        self.Duration_in_number_of_seconds = Duration_in_number_of_seconds
        self.Updated_time = Updated_time


class podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name_of_the_podcast = db.Column(db.String(100), nullable=False)
    Duration_in_number_of_seconds = db.Column(db.Float, nullable=False)
    Updated_time = db.Column(db.DateTime, nullable=False)
    Host = db.Column(db.String(100), nullable=False)
    Participants = db.Column(db.String(100), nullable=True)

    def __init__(self, Name_of_the_podcast, Duration_in_number_of_seconds,
                 Updated_time, Host, Participants):

        self.Name_of_the_podcast = Name_of_the_podcast
        self.Duration_in_number_of_seconds = Duration_in_number_of_seconds
        self.Updated_time = Updated_time
        self.Host = Host
        self.Participants = Participants


class audiobook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title_of_the_audiobook = db.Column(db.String(100), nullable=False)
    Author_of_the_audiobook = db.Column(db.String(100), nullable=False)
    Narrator = db.Column(db.String(100), nullable=False)
    Duration_in_number_of_seconds = db.Column(db.Float, nullable=False)
    Updated_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, Title_of_the_audiobook, Author_of_the_audiobook, Narrator, Duration_in_number_of_seconds, Updated_time):

        self.Title_of_the_audiobook = Title_of_the_audiobook
        self.Author_of_the_audiobook = Author_of_the_audiobook
        self.Narrator = Narrator
        self.Duration_in_number_of_seconds = Duration_in_number_of_seconds
        self.Updated_time = Updated_time


class AllSchema(ma.Schema):
    class Meta:  # To Show which field
        fields = ('id', 'Name_of_the_song', 'Name_of_the_podcast', 'Host', 'Participants', 'Title_of_the_audiobook', 'Author_of_the_audiobook', 'Narrator',
                  'Duration_in_number_of_seconds', 'Updated_time')
