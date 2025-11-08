from __future__ import annotations

import pytest

from flowforge.version import get_latest_major_versions


@pytest.fixture(autouse=True)
def _reset_cache() -> None:
    get_latest_major_versions.cache_clear()


###############################################
#     Tests for get_latest_major_versions     #
###############################################


def test_get_latest_major_versions_requests() -> None:
    assert get_latest_major_versions("requests", upper="2.30") == ("0.14.2", "1.2.3", "2.29.0")


def test_get_latest_major_versions_torch() -> None:
    assert get_latest_major_versions("torch", upper="2.9") == ("1.13.1", "2.8.0")
