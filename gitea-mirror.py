import os.path
import sys
from src.gitea_api import GiteaApi
from src.repository_name import get_repository_name, is_valid_repository_names
from src.config import Config, read_ini_config
from src.models import GiteaRepository
from src.git import git_pull, git_clone

from os import makedirs

BASE_PATH = "out"
FORMAT = "{owner}/{name}"


def process_repo(config: Config, repo: GiteaRepository):
    path = get_repository_name(name_format=config.repository_format, r=repo)
    out_path = os.path.join(config.out_dir, path)
    makedirs(out_path, exist_ok=True)
    if os.path.exists(os.path.join(out_path, ".git")):
        git_pull(out_path, ssh_key="fake")
        return
    print(f"New repository: {path}")
    git_clone(ssh_url=repo.ssh_url, repository=out_path, ssh_key="fake")


def main():
    if len(sys.argv) < 2:
        print("Usage: python gitea-mirror.py CONFIG_PATH")
        sys.exit(1)
    try:
        config = read_ini_config(sys.argv[1])
    except RuntimeError as err:
        print(f"Invalid config: {err}")
        sys.exit(1)

    api = GiteaApi(
        endpoint=config.endpoint,
        token=config.token,
    )
    repos = api.get_repositories()
    print(f"total {len(repos)} repositories")

    if not is_valid_repository_names(name_format=config.repository_format, repos=repos):
        print("Format string is not valid, duplicates are not allowed")
        sys.exit(1)

    for repo in repos:
        process_repo(config=config, repo=repo)


if __name__ == "__main__":
    main()
