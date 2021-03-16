from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from audio import AllSchema, song, podcast, audiobook, db
import os
database = os.environ['SECRET_KEY']
app = Flask(__name__)


all_schema = AllSchema()  # one Product
alls_schema = AllSchema(many=True)  # Many Products

app.config['SQLALCHEMY_DATABASE_URI'] = database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

# Post


@ app.route('/<string:audioFiletype>', methods=['POST'])
def add_product(audioFiletype):
    try:

        if audioFiletype == 'song':

            Name_of_the_song = request.json['Name_of_the_song']
            Duration_in_number_of_seconds = request.json['Duration_in_number_of_seconds']
            Updated_time = request.json['Updated_time']

            if (len(str(Name_of_the_song)) > 0 and int(Duration_in_number_of_seconds) >= 0 and len(str(Updated_time)) > 0):

                # print(Name_of_the_song, Duration_in_number_of_seconds, Updated_time)
                new_song = song(Name_of_the_song,
                                Duration_in_number_of_seconds, Updated_time)

                db.session.add(new_song)
                db.session.commit()

                ap = all_schema.jsonify(new_song)  # single product

                return all_schema.jsonify(new_song)
            else:
                return ("Bad Request", 400)

        elif audioFiletype == 'podcast':
            Name_of_the_podcast = request.json['Name_of_the_podcast']
            Duration_in_number_of_seconds = request.json['Duration_in_number_of_seconds']
            Updated_time = request.json['Updated_time']
            Host = request.json['Host']

            if (len(str(Name_of_the_podcast)) > 0 and int(Duration_in_number_of_seconds) >= 0 and len(str(Updated_time)) > 0 and len(str(Host)) > 0):
                try:
                    Participants = request.json['Participants']
                    if(len(Participants) <= 10):
                        new_podcast = podcast(Name_of_the_podcast,
                                              Duration_in_number_of_seconds, Updated_time, Host, Participants)
                    else:
                        return ("Bad Request", 400)
                except KeyError:
                    new_podcast = podcast(Name_of_the_podcast,
                                          Duration_in_number_of_seconds, Updated_time, Host, None)
                except:
                    return
                db.session.add(new_podcast)
                db.session.commit()

                return all_schema.jsonify(new_podcast)

            else:
                return ("Bad Request", 400)

        elif audioFiletype == 'audiobook':
            Title_of_the_audiobook = request.json['Title_of_the_audiobook']
            Author_of_the_audiobook = request.json['Author_of_the_audiobook']
            Narrator = request.json['Narrator']
            Duration_in_number_of_seconds = request.json['Duration_in_number_of_seconds']
            Updated_time = request.json['Updated_time']
            if (len(str(Title_of_the_audiobook)) > 0 and len(str(Author_of_the_audiobook)) > 0 and len(str(Narrator)) > 0 and int(Duration_in_number_of_seconds) >= 0 and len(str(Updated_time)) > 0):

                new_audiobook = audiobook(Title_of_the_audiobook, Author_of_the_audiobook,
                                          Narrator, Duration_in_number_of_seconds, Updated_time)
                db.session.add(new_audiobook)
                db.session.commit()

                return all_schema.jsonify(new_audiobook)

            else:
                return "bad request", 400
    except:
        return "internal server error", 500

# GET


@ app.route('/<string:audioFiletype>', methods=['GET'])
def get_products(audioFiletype):

    try:

        if audioFiletype == 'song':
            songget = song.query.all()

            result = alls_schema.dump(songget)
            return jsonify(result)
        elif audioFiletype == 'podcast':
            podcast1 = podcast.query.all()
            result = alls_schema.dump(podcast1)
            return jsonify(result)
        elif audioFiletype == 'audiobook':
            audiobook1 = audiobook.query.all()
            result = alls_schema.dump(audiobook1)
            return jsonify(result)
        else:
            return "bad request", 400
    except:
        return "internal server error", 500


@ app.route('/<string:audioFiletype>/<id>', methods=['GET'])
def get_product(audioFiletype, id):

    try:

        if audioFiletype == 'song':
            songget = song.query.get(id)
            return all_schema.jsonify(songget)
        elif audioFiletype == 'podcast':
            podcast1 = podcast.query.get(id)
            return all_schema.jsonify(podcast1)
        elif audioFiletype == 'audiobook':
            audiobook1 = audiobook.query.get(id)
            return all_schema.jsonify(audiobook1)
        else:
            return "bad request", 400
    except:
        return "internal server error", 500


# Delete

@app.route('/audioFiletype/<id>', methods=['DELETE'])
def delete_product(audioFiletype, id):

    try:
        audioFiletype = request.json['audioFiletype']

        if audioFiletype == 'song':
            product = song.query.get(id)
            db.session.delete(product)
            db.session.commit()
            return all_schema.jsonify(product)
        elif audioFiletype == 'podcast':
            podcast1 = podcast.query.get(id)
            db.session.delete(podcast1)
            db.session.commit()
            return all_schema.jsonify(podcast1)
        elif audioFiletype == 'audiobook':
            audiobook1 = audiobook.query.get(id)
            db.session.delete(audiobook1)
            db.session.commit()
            return all_schema.jsonify(audiobook1)
        else:
            return "bad request", 400
    except:
        return "internal server error", 500

# Update


@app.route('/<string:audioFiletype>/<id>', methods=['PUT'])
def update_product(audioFiletype, id):
    try:
        if audioFiletype == 'song':
            songget1 = song.query.get(id)

            Name_of_the_song = request.json['Name_of_the_song']
            Duration_in_number_of_seconds = request.json['Duration_in_number_of_seconds']
            Updated_time = request.json['Updated_time']
            if (len(str(Name_of_the_song)) > 0 and int(Duration_in_number_of_seconds) >= 0 and len(str(Updated_time)) > 0):

                songget1.Name_of_the_song = Name_of_the_song
                songget1.Duration_in_number_of_seconds = Duration_in_number_of_seconds
                songget1.Updated_time = Updated_time

                new_procduct = song(
                    Name_of_the_song, Duration_in_number_of_seconds, Updated_time)
                db.session.commit()
                return all_schema.jsonify(new_procduct)  # single product
            else:
                return "bad request", 400

        elif audioFiletype == 'podcast':
            podcast1 = podcast.query.get(id)

            Name_of_the_podcast = request.json['Name_of_the_podcast']
            Duration_in_number_of_seconds = request.json['Duration_in_number_of_seconds']
            Updated_time = request.json['Updated_time']
            Host = request.json['Host']
            if (len(str(Name_of_the_podcast)) > 0 and int(Duration_in_number_of_seconds) >= 0 and len(str(Updated_time)) > 0 and len(str(Host)) > 0):
                podcast1.Name_of_the_podcast = Name_of_the_podcast
                podcast1.Duration_in_number_of_seconds = Duration_in_number_of_seconds
                podcast1.Updated_time = Updated_time
                podcast1.Host = Host
                try:
                    Participants = request.json['Participants']

                    podcast1.Participants = Participants

                    new_podcast = podcast(
                        Name_of_the_podcast, Duration_in_number_of_seconds, Updated_time, Host, Participants)

                except KeyError:
                    podcast1.Participants = None

                    new_podcast = podcast(
                        Name_of_the_podcast, Duration_in_number_of_seconds, Updated_time, Host, None)

                db.session.commit()
                return all_schema.jsonify(new_podcast)  # single product

            else:
                return "bad request", 400

        elif audioFiletype == 'audiobook':
            audiobook1 = audiobook.query.get(id)

            Title_of_the_audiobook = request.json['Title_of_the_audiobook']
            Author_of_the_audiobook = request.json['Author_of_the_audiobook']
            Narrator = request.json['Narrator']
            Duration_in_number_of_seconds = request.json['Duration_in_number_of_seconds']
            Updated_time = request.json['Updated_time']
            if (len(str(Title_of_the_audiobook)) > 0 and len(str(Author_of_the_audiobook)) > 0 and len(str(Narrator)) > 0 and int(Duration_in_number_of_seconds) >= 0 and len(str(Updated_time)) > 0):

                audiobook1.Title_of_the_audiobook = Title_of_the_audiobook
                audiobook1.Author_of_the_audiobook = Author_of_the_audiobook
                audiobook1.Narrator = Narrator
                audiobook1.Duration_in_number_of_seconds = Duration_in_number_of_seconds
                audiobook1.Updated_time = Updated_time

                new_audiobook = audiobook(Title_of_the_audiobook, Author_of_the_audiobook,
                                          Narrator, Duration_in_number_of_seconds, Updated_time)
                db.session.commit()
                return all_schema.jsonify(new_audiobook)  # single product

            else:
                return "bad request", 400
    except:
        return "internal server error", 500


if __name__ == '__main__':
    app.run(debug=True)
