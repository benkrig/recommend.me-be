import json
from util.logs import logger
from util.endpoints import endpoints
from util.response import generate_response, generate_error


def universal(event, context):
    try:
        logger.info('Received event: {}'.format(json.dumps(event, indent=2)))

        payload = {
            'q': event.get('queryStringParameters'),
            'b': event.get('body')
        }

        if event['path'] in endpoints:

            return generate_response(endpoints[event['path']](payload))
        else:
            raise ValueError('Unrecognized endpoint "{}"'.format(event['path']))
    except Exception as e:
        logger.info(e)
        return generate_error()


if __name__ == "__main__":
    ev = {
        'path': '/recommendmeFE-dev-universal/',
        'queryStringParameters': {
            'q': 'asd'
        }
    }
    res = universal(ev, None)
    print(res)
