from db.search import search
from db.default import default

prefix = '/recommendmeFE-dev-universal'

endpoints = {
    '/search': lambda payload: search(payload['q']),
    '/': lambda payload: default(),
    '': lambda payload: default()
}