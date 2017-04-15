from django.db import models

from app_server.enums import JobStatus


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, default='')
    git_url = models.CharField(max_length=240, unique=True)


class Commit(BaseModel):
    commit_id = models.CharField(max_length=100)
    project = models.ForeignKey(Project, related_name='commits')
    author = models.CharField(max_length=100)

    class Meta:
        unique_together = ('commit_id', 'project')


class ProjectJob(BaseModel):
    project = models.ForeignKey(Project, related_name='project_jobs')
    status = models.CharField(max_length=50, choices=JobStatus.choices(), default=JobStatus.CREATED)
    name = models.CharField(max_length=100, blank=True, default='')
    total_commits = models.IntegerField(default=0)
    processed_commits = models.IntegerField(default=0)
    error_log = models.TextField(blank=True, default='')


class CommitJob(BaseModel):
    commit = models.ForeignKey(Commit, related_name='commit_jobs')
    project_job = models.ForeignKey(ProjectJob, related_name='commit_jobs')
    status = models.CharField(max_length=50, choices=JobStatus.choices(), default=JobStatus.CREATED)
    error_log = models.TextField(blank=True, default='')


class File(BaseModel):
    project = models.ForeignKey(Project, related_name='files')
    name = models.CharField(max_length=100)
    ext = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    path = models.CharField(max_length=255)

    class Meta:
        unique_together = ('project', 'path')


class FileMapping(BaseModel):
    project_job = models.ForeignKey(ProjectJob, related_name='file_mappings')
    file_from = models.ForeignKey(File, related_name='files_to')
    file_to = models.ForeignKey(File, related_name='files_from')
    weight = models.FloatField(default=0)

    class Meta:
        unique_together = ('project_job', 'file_from', 'file_to')
