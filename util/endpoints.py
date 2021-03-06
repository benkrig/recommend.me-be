from db.search import search
from db.default import default

endpoints = {
    '/search': lambda payload: search(payload['q']),
    '/': lambda payload: default()
}