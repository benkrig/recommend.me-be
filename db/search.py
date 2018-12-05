from util.logs import logger
from util.connection import Neo4jConnection
from json import *

# Search movies query
s_movies = "MATCH (movie:Movie) WHERE movie.title =~ {title} RETURN movie"

# TODO: Search actors query
s_actors = None


def search(q):
    try:
        conn = Neo4jConnection().get_db()

        results = conn.run(s_movies, {"title": "(?i).*" + q + ".*"})

        return dumps([serialize_movie(record['movie']) for record in results])
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


# TODO: serialize_actor
def serialize_actor(actor):
    return {}