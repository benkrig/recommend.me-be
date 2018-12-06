from util.logs import logger
from util.connection import Neo4jConnection
from json import *

# Search movies query
s_movies = "MATCH (movie:Movie) WHERE movie.title =~ {title} RETURN movie"

s_persons = "MATCH (person:Person) where person.name =~ {name} RETURN person"


def search(q):
    try:
        conn = Neo4jConnection().get_db()

        movies = conn.run(s_movies, {"title": "(?i).*" + q + ".*"})
        persons = conn.run(s_persons, {"name": "(?i).*" + q + ".*"})

        results = {
            "movies": [serialize_movie(movie['movie']) for movie in movies],
            "actors": [serialize_person(person['person']) for person in persons]
        }

        return dumps(results)
    except Exception as e:
        logger.error(e)
        raise
    finally:
        Neo4jConnection().close_db()


def serialize_movie(movie):
    return {
        'id': movie['id'],
        'title': movie['title'],
        'summary': movie['summary'],
        'released': movie['released'],
        'duration': movie['duration'],
        'rated': movie['rated'],
        'tagline': movie['tagline']
    }


def serialize_person(person):
    return {
        'id': person['id'],
        'name': person['name'],
        'born': person['born']
    }
