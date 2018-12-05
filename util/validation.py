

def get_payload(event):
    """Utility to retrieve q and body from the AWS Lambda event object
    :param event:
    :return: {}
    """
    query_string_parameters = event.get("queryStringParameters")
    body = event.get("body")

    payload = {}

    if query_string_parameters:
        payload['q'] = query_string_parameters.get('q')
    if body:
        payload['body'] = body
    return payload