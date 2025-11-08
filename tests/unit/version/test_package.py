from __future__ import annotations

from unittest.mock import Mock, patch

import pytest

from flowforge.version import get_latest_major_versions


@pytest.fixture(autouse=True)
def _reset_cache() -> None:
    get_latest_major_versions.cache_clear()


###############################################
#     Tests for get_latest_major_versions     #
###############################################


def test_get_latest_major_versions() -> None:
    mock = Mock(return_value=("0.1.0", "0.8.0", "0.9.0", "1.0.0", "1.2.0", "1.3.0", "2.0.0"))
    with patch("flowforge.version.package.get_pypi_versions", mock):
        assert get_latest_major_versions("my_package") == ("0.9.0", "1.3.0", "2.0.0")


def test_get_latest_major_versions_lower() -> None:
    mock = Mock(return_value=("0.1.0", "0.8.0", "0.9.0", "1.0.0", "1.2.0", "1.3.0", "2.0.0"))
    with patch("flowforge.version.package.get_pypi_versions", mock):
        assert get_latest_major_versions("my_package", lower="1.0.0") == ("1.3.0", "2.0.0")


def test_get_latest_major_versions_upper() -> None:
    mock = Mock(return_value=("0.1.0", "0.8.0", "0.9.0", "1.0.0", "1.2.0", "1.3.0", "2.0.0"))
    with patch("flowforge.version.package.get_pypi_versions", mock):
        assert get_latest_major_versions("my_package", upper="2.0.0") == ("0.9.0", "1.3.0")


def test_get_latest_major_versions_range() -> None:
    mock = Mock(return_value=("0.1.0", "0.8.0", "0.9.0", "1.0.0", "1.2.0", "1.3.0", "2.0.0"))
    with patch("flowforge.version.package.get_pypi_versions", mock):
        assert get_latest_major_versions("my_package", lower="1.0.0", upper="2.0.0") == ("1.3.0",)
