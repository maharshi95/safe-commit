from django.db import models


# Create your models here.
from django.utils import timezone


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
