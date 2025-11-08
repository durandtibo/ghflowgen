from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import Mock, patch

import pytest

from flowforge.utils.export import generate_unique_tmp_path, save_json

if TYPE_CHECKING:
    from pathlib import Path


###############################
#     Tests for save_json     #
###############################


def test_save_json(tmp_path: Path) -> None:
    path = tmp_path.joinpath("tmp/data.json")
    save_json({"key1": [1, 2, 3], "key2": "abc"}, path)
    assert path.is_file()


def test_save_json_file_exist(tmp_path: Path) -> None:
    path = tmp_path.joinpath("tmp/data.json")
    save_json({"key1": [1, 2, 3], "key2": "abc"}, path)
    with pytest.raises(FileExistsError, match=r"path .* already exists."):
        save_json({"key1": [1, 2, 3], "key2": "abc"}, path)


def test_save_json_file_exist_ok(tmp_path: Path) -> None:
    path = tmp_path.joinpath("tmp/data.json")
    save_json({"key1": [1, 2, 3], "key2": "abc"}, path)
    save_json({"key1": [3, 2, 1], "key2": "meow"}, path, exist_ok=True)
    assert path.is_file()


def test_save_json_file_exist_ok_dir(tmp_path: Path) -> None:
    path = tmp_path.joinpath("tmp/data.json")
    path.mkdir(parents=True, exist_ok=True)
    with pytest.raises(IsADirectoryError, match=r"path .* is a directory"):
        save_json({"key1": [1, 2, 3], "key2": "abc"}, path)


##############################################
#     Tests for generate_unique_tmp_path     #
##############################################


def test_generate_unique_tmp_path_no_suffix(tmp_path: Path) -> None:
    with patch("flowforge.utils.export.uuid.uuid4", lambda: Mock(hex="a1b2c3")):
        assert generate_unique_tmp_path(tmp_path.joinpath("data")) == tmp_path.joinpath(
            "data-a1b2c3"
        )


def test_generate_unique_tmp_path_one_suffix(tmp_path: Path) -> None:
    with patch("flowforge.utils.export.uuid.uuid4", lambda: Mock(hex="a1b2c3")):
        assert generate_unique_tmp_path(tmp_path.joinpath("data.json")) == tmp_path.joinpath(
            "data-a1b2c3.json"
        )


def test_generate_unique_tmp_path_two_suffixes(tmp_path: Path) -> None:
    with patch("flowforge.utils.export.uuid.uuid4", lambda: Mock(hex="a1b2c3")):
        assert generate_unique_tmp_path(tmp_path.joinpath("data.tar.gz")) == tmp_path.joinpath(
            "data-a1b2c3.tar.gz"
        )


def test_generate_unique_tmp_path_dir(tmp_path: Path) -> None:
    with patch("flowforge.utils.export.uuid.uuid4", lambda: Mock(hex="a1b2c3")):
        assert generate_unique_tmp_path(tmp_path.joinpath("data/")) == tmp_path.joinpath(
            "data-a1b2c3"
        )
