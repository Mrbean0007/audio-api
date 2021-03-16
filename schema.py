import psycopg2

conn = psycopg2.connect(database="audio", user="postgres",
                        password="531998", host="127.0.0.1", port="5432")


cur = conn.cursor()
cur.execute('''CREATE TABLE songs (id smallserial PRIMARY KEY NOT NULL,
                              Name_of_the_song VARCHAR(100) NOT NULL,
                              Duration_in_number_of_seconds smallserial NOT NULL,
                              Updated_time timestamp NOT NULL );''')

cur.execute('''CREATE TABLE podcast (id smallserial PRIMARY KEY NOT NULL,
                              Name_of_the_podcast VARCHAR(100) NOT NULL, 
                              Duration_in_number_of_seconds smallserial NOT NULL,
                              Updated_time timestamp NOT NULL,
                              Host VARCHAR(100) NOT NULL,
                              Participants VARCHAR(100) NULL);''')

cur.execute('''CREATE TABLE audiobook (id smallserial PRIMARY KEY NOT NULL,
                              Title_of_the_audiobook VARCHAR(100) NOT NULL, 
                              Author_of_the_audiobook VARCHAR(100) NOT NULL, 
                              Narrator VARCHAR(100) NOT NULL, 
                              Duration_in_number_of_seconds smallserial NOT NULL,
                              Updated_time timestamp NOT NULL);''')


conn.commit()
cur.close()
conn.close()
