import datetime
from typing import List

from .models import GiteaRepository, GiteaUser


def _get_test_repository() -> GiteaRepository:
    return GiteaRepository(
        ssh_url="ssh://git@example.com/project/name",
        name="test name",
        id=42,
        updated_at=datetime.datetime.now(),
        owner=GiteaUser(
            id=23,
            login="test_user",
            email="test_user@example.com",
        ),
    )


def is_valid_format(name_format: str) -> bool:
    try:
        get_repository_name(name_format, _get_test_repository())
    except KeyError:
        return False
    return True


def get_repository_name(name_format: str, r: GiteaRepository) -> str:
    return name_format.format(
        name=r.name,
        repository_id=r.repo_id,
        owner=r.owner.login,
        owner_id=r.owner.user_id,
    )


def is_valid_repository_names(name_format: str, repos: List[GiteaRepository]):
    names = set(get_repository_name(name_format, r) for r in repos)
    return len(names) == len(repos)  # all names must be unique
