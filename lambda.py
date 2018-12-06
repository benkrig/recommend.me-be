import json
from util.logs import logger
from util.endpoints import endpoints
from util.response import generate_response, generate_error
from util.validation import get_payload


def universal(event, context):
    try:
        logger.info('Received event: {}'.format(json.dumps(event, indent=2)))

        payload = get_payload(event)

        if event['path'] in endpoints:
            return generate_response(endpoints[event['path']](payload))
        else:
            raise ValueError('Unrecognized endpoint "{}"'.format(event['path']))
    except Exception as e:
        logger.info(e)
        return generate_error()


if __name__ == "__main__":
    ev = {
        'path': '/search',
        "queryStringParameters": { "q": "tom" }
    }
    res = universal(ev, None)
    print(res)
