import json

from util.logs import logger

OK = 200


def generate_response(body):
    """Utility for generating a JSON response for AWS Lambda.
    :param body:
    :return:
    """
    try:
        r = {
            'statusCode': OK,
            'body': json.dumps(body),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
        return r
    except Exception as e:
        logger.error(e)
        return


def generate_error():
    """Utility for generating a generic error response for AWS Lambda.
    :return:
    """
    return {
        'statusCode': 500,
        'body': json.dumps({
            'message': 'There was a problem servicing the request.'
        })
    }
