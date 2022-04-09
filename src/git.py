import subprocess
from os import makedirs


def git_clone(ssh_url: str, repository: str, ssh_key: str) -> bool:
    makedirs(repository, exist_ok=True)
    try:
        subprocess.check_call(
            ["git", "clone", ssh_url, "."], cwd=repository
        )
    except subprocess.CalledProcessError:
        print(f"Unable to clone repository {repository} with key {ssh_key} from {ssh_url}")
        return False
    return True


def git_pull(repository: str, ssh_key: str) -> bool:
    try:
        subprocess.check_call(["git", "pull"], cwd=repository)
    except subprocess.CalledProcessError:
        print(f"Unable to pull repository {repository} with key {ssh_key}")
        return False
    return True
