import json
from typing import Dict

from flask import Response


def json_response(status: int = 200, response_data: Dict = None) -> Response:
    """
    Returns HTTP response with JSON body
    """
    headers = {"Content-Type": "application/json"}

    if response_data is None:
        response = None
    else:
        response = json.dumps(response_data, default=str)

    return Response(status=status, response=response, headers=headers)
