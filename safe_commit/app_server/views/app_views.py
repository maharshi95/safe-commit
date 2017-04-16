from django.http.response import JsonResponse


# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view

from app_server.views.utils import wrapped_json_response


@api_view(http_method_names=['GET'])
def health_api(request):
    return wrapped_json_response(status=status.HTTP_200_OK, message="Greetings from safe-commit :)")
