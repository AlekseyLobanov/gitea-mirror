from typing import List
from urllib.parse import urljoin

import requests
from pydantic import parse_obj_as

from .models import GiteaRepository


class GiteaApi:
    def __init__(self, endpoint: str, token: str):
        self._endpoint = endpoint
        self._token = token

    def get_repositories(self, page_size=10) -> List[GiteaRepository]:
        """
        For mirroring input user is not important.
        """
        session = requests.session()
        session.headers.update({"Authorization": "token " + self._token})
        all_repos = {}  # hack for unique repositories in result
        page_id = 1
        while True:
            r = session.get(
                urljoin(
                    self._endpoint,
                    f"/api/v1/user/repos",
                ),
                params={"limit": page_size, "page": page_id},
            )
            if r.status_code != 200:
                print(f"Failed request, code {r.status_code}")
                return []
            repos_data = r.json()
            if not repos_data:
                break
            else:
                page_id += 1
            cur_repos = parse_obj_as(List[GiteaRepository], repos_data)
            for repo in cur_repos:
                all_repos[repo.repo_id] = repo
        return list(all_repos.values())
