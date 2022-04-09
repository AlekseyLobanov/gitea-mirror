from tempfile import NamedTemporaryFile

from src.config import read_ini_config, Config

import pytest


@pytest.mark.parametrize(
    "config_data, expected",
    [
        (
            "[main]\ntoken=something\n"
            "format={owner}/{name}\n"
            "ssh_key=/tmp/no_key\n"
            "endpoint=https://example.com\n"
            "out_dir=/home/user/repositories",
            Config(
                token="something",
                repository_format="{owner}/{name}",
                out_dir="/home/user/repositories",
endpoint="https://example.com",
ssh_key_path="/tmp/no_key"
            ),
        ),
        ("[main]", None),
    ],
)
def test_ini_config(config_data, expected):
    with NamedTemporaryFile() as tf:
        if config_data:
            tf.write(config_data.encode("utf-8"))
            tf.flush()
        if expected:
            assert read_ini_config(tf.name) == expected
        else:
            with pytest.raises(RuntimeError):
                read_ini_config(tf.name)


def test_ini_config_not_exists():
    with pytest.raises(RuntimeError):
        read_ini_config("not_existing_file")
