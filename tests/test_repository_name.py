import pytest
from src.repository_name import is_valid_format


@pytest.mark.parametrize(
    "name_format, expected",
    [
        ("{blabla}", False),
        ("", True),
        ("{owner}/{name}", True),
    ]
)
def test_name_formatting(name_format, expected):
    assert is_valid_format(name_format) == expected