import json
from util.logs import logger
from util.endpoints import endpoints


def universal(event, context):
    try:
        logger.info('Received event: {}'.format(json.dumps(event, indent=2)))

        payload = {
            'q': event.get('queryStringParameters'),
            'b': event.get('body')
        }

        if event['path'] in endpoints:
            return endpoints[event['path']](payload)
        else:
            raise ValueError('Unrecognized endpoint "{}"'.format(event['path']))
    except Exception as e:
        logger.info(e)
        return {'asd': 'asd'}

if __name__ == "__main__":
    ev = {
        'path': '/recommendmeFE-dev-univerasdsal',
        'queryStringParameters': {
            'q': 'asd'
        }
    }
    res = universal(ev, None)
    print(res)
