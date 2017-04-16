# Author: Maharshi Gor
from django.http.response import JsonResponse
from rest_framework import status as http_status


def wrapped_json_response(status=http_status.HTTP_200_OK, message='', data=None):
    data = data or None
    return JsonResponse(status=status, data={
        'status': 'Success' if http_status.is_success(status) else 'Error',
        'message': message,
        'data': data
    })
