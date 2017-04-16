import os.path as osp

from app_worker import constants

from django.db import models

from app_server.enums import JobStatus, FileType


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

    @property
    def space_ecs_name(self):
        return self.name.replace(' ', '_')

    @property
    def repo_name(self):
        git_url = self.project.git_url
        return git_url.split('/')[-1][:-4]

    @property
    def local_dir_name(self):
        return 'job-{}_project-{}_{}'.format(self.id, self.project_id, self.space_ecs_name)

    @property
    def local_dir_path(self):
        return osp.join(constants.DATA_PATH, self.local_dir_name)

    @property
    def repo_path(self):
        return osp.join(self.local_dir_path, constants.JOB_REPO_DIR_NAME)



class CommitJob(BaseModel):
    commit = models.ForeignKey(Commit, related_name='commit_jobs')
    project_job = models.ForeignKey(ProjectJob, related_name='commit_jobs')
    status = models.CharField(max_length=50, choices=JobStatus.choices(), default=JobStatus.CREATED)
    error_log = models.TextField(blank=True, default='')


class File(BaseModel):
    project = models.ForeignKey(Project, related_name='files')
    name = models.CharField(max_length=100)
    ext = models.CharField(max_length=10)
    type = models.CharField(max_length=50, choices=FileType.choices())
    path = models.CharField(max_length=255)

    @property
    def full_name(self):
        return '{}.{}'.format(self.name, self.ext)

    class Meta:
        unique_together = ('project', 'path')


class FileMapping(BaseModel):
    project_job = models.ForeignKey(ProjectJob, related_name='file_mappings')
    file_from = models.ForeignKey(File, related_name='files_to')
    file_to = models.ForeignKey(File, related_name='files_from')
    weight = models.FloatField(default=0)

    class Meta:
        unique_together = ('project_job', 'file_from', 'file_to')
