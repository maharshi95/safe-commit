# Author: Maharshi Gor
import logging
from git.repo.base import Repo

from app_server.models import ProjectJob
from commons.utils import bash_utils

logger = logging.getLogger(__name__)

class ProjectJobUtils:

    @staticmethod
    def clone_repo(project_job: ProjectJob):
        logger.info('creating the dirs...')
        bash_utils.create_dirs(project_job.repo_path)
        logger.info('path: {}'.format(project_job.repo_path))
        logger.info('cloning the repo')
        bash_utils.bash('cd {} && git clone -v {}'.format(project_job.repo_path, project_job.git_url))
        # Repo.clone_from(project_job.git_url, project_job.repo_path)