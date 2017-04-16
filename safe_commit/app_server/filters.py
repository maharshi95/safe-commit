# Author: Maharshi Gor
import django_filters
from django_filters.rest_framework import FilterSet

from app_server.enums import JobStatus
from app_server.models import ProjectJob


class ProjectJobFilter(FilterSet):
    status = django_filters.ChoiceFilter(choices=JobStatus.values(), required=False)
    project_id = django_filters.NumberFilter()
    status_name = django_filters.CharFilter(name='status', lookup_expr='iexact')
    class Meta:
        model = ProjectJob
        fields = ('name', 'status', 'project_id')
