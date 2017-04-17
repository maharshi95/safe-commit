# Author: Maharshi Gor
# from __future__ import absolute_import
import logging

from app_server.models import ProjectJob
from app_worker.utils.project_job_utils import ProjectJobUtils
from safe_commit.celery import app

logger = logging.getLogger(__name__)

@app.task(name='factorial')
def factorial(n: int):
    p = 1
    for i in range(1, n + 1):
        p *= i
    print('{}! = {}'.format(n, p))
    return p


@app.task(name='run_job')
def run_project_job(job_id: int):
    logger.info("Getting Job from db")
    project_job = ProjectJob.objects.get(id=job_id)
    logger.info("Got the Job from db: {}".format(project_job.id))
    logger.info("Cloning th repo...")
    ProjectJobUtils.clone_repo(project_job)
