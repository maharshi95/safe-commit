# Author: Maharshi Gor

def get_user_from_url(git_url: str):
    return git_url.split('/')[-2]


def get_repo_name(git_url: str):
    return git_url.split('/')[-1][:-4]

