import json
import logging

from util.endpoints import endpoints, prefix

logging.basicConfig(level=logging.INFO)


def universal(event, context):
    try:
        logging.info('Received event: {}'.format(json.dumps(event, indent=2)))

        payload = {
            'q': event.get('queryStringParameters'),
            'b': event.get('body')
        }

        if event['path'] in endpoints:
            return endpoints[event['path']](payload)
        else:
            raise ValueError('Unrecognized endpoint "{}"'.format(event['path']))
    except Exception as e:
        print(e)
        logging.error(e)
        return e


if __name__ == "__main__":
    ev = {
        'path': '/recommendmeFE-dev-univerasdsal',
        'queryStringParameters': {
            'q': 'asd'
        }
    }
    res = universal(ev, None)
    print(res)
