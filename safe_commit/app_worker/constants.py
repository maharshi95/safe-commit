# Author: Maharshi Gor
import os.path as osp

from safe_commit.configurations.configs import PROJECT_DATA_DIR_NAME
from safe_commit.settings import configs

BASE_DIR_PATH = configs.base_dir_path
DATA_PATH = osp.join(BASE_DIR_PATH, PROJECT_DATA_DIR_NAME)
JOB_REPO_DIR_NAME = 'repo'
