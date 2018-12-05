from db.search import search
from db.default import default

prefix = '/recommendmeFE-dev-universal'

endpoints = {
    prefix + '/search': lambda payload: search(payload['q']),
    prefix + '/': lambda payload: default(),
    prefix + '': lambda payload: default()
}