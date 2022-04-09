"""
Token should be treated as password,
files are more secure in general than command-line arguments

.ini config example
[main]
endpoint=https://example.com/gitea
token=something
format={owner}/{name}
out_dir=/home/user/repositories
ssh_key=/home/user/.ssh/id_rsa.pub

"""

import configparser
import os

from .models import Config

MAIN_SECTION = "main"


def read_ini_config(path: str) -> Config:
    if not os.path.exists(path):
        raise RuntimeError("INI config path is not exists")

    parser = configparser.ConfigParser()
    parser.read(path)
    try:
        endpoint = parser[MAIN_SECTION]["endpoint"]
        token = parser[MAIN_SECTION]["token"]
        repository_format = parser[MAIN_SECTION]["format"]
        out_dir = parser[MAIN_SECTION]["out_dir"]
        ssh_key_path = parser[MAIN_SECTION]["ssh_key"]
    except KeyError as err:
        raise RuntimeError(f"No value for section: {err}")

    return Config(
        repository_format=repository_format,
        endpoint=endpoint,
        token=token,
        out_dir=out_dir,
        ssh_key_path=ssh_key_path,
    )
