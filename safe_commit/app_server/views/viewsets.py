# Author: Maharshi Gor
import traceback

from django.db.utils import OperationalError, IntegrityError, NotSupportedError
from rest_framework import status
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from app_server.filters import ProjectJobFilter
from app_server.models import Project, ProjectJob
from app_server.serializers import ProjectJobSerializer, ProjectElaborateSerializer
from app_server.views.utils import wrapped_json_response


class ProjectListCreateAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectElaborateSerializer

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)

        except (IntegrityError, NotSupportedError) as ex:
            traceback.print_exc()
            return wrapped_json_response(status.HTTP_400_BAD_REQUEST, message=str(ex))

        except OperationalError as ex:
            traceback.print_exc()
            return wrapped_json_response(status.HTTP_503_SERVICE_UNAVAILABLE, message=str(ex))

        except Exception as ex:
            traceback.print_exc()
            return wrapped_json_response(status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(ex))


class RetrieveProjectAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectElaborateSerializer
    lookup_field = 'id'


class ProjectJobListCreateView(ListCreateAPIView):
    queryset = ProjectJob.objects.all()
    serializer_class = ProjectJobSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ProjectJobFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProjectJobRetrieveAPIView(RetrieveAPIView):
    queryset = ProjectJob.objects.all()
    serializer_class = ProjectJobSerializer
    lookup_field = 'id'
