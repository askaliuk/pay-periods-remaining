from flask import jsonify


def validation_error(error):
    message = {
        'status': 400,
        'message': error
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp
