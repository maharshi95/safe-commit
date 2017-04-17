# Author: Maharshi Gor
from rest_framework import serializers

from app_server.enums import JobStatus
from app_server.models import Project, ProjectJob


class ProjectBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'git_url')


class ProjectElaborateSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField(default='')
    git_url = serializers.URLField()
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'git_url')


class ProjectJobSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    status = serializers.ChoiceField(choices=JobStatus.values(), read_only=True)
    total_commits = serializers.IntegerField(read_only=True)
    processed_commits = serializers.IntegerField(read_only=True)
    project_id = serializers.IntegerField(write_only=True)
    project = ProjectBriefSerializer(read_only=True)

    class Meta:
        model = ProjectJob
        fields = ('id', 'project', 'project_id', 'status', 'name', 'total_commits', 'processed_commits')
        depth = 1
