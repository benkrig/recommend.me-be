import json
import logging

from util.endpoints import endpoints

logging.basicConfig(level=logging.INFO)


def universal(event, context):
    logging.info('Received event: {}'.format(json.dumps(event, indent=2)))

    payload = {
        'q': event.get('queryStringParameters'),
        'b': event.get('body')
    }

    if event['path'] in endpoints:
        return endpoints[event['path']](payload)
    else:
        raise ValueError('Unrecognized endpoint "{}"'.format(event['path']))


if __name__ == "__main__":
    e = {
        'path': '/',
        'queryStringParameters': {
            'q': 'asd'
        }
    }
    res = universal(e, None)
    print(res)
