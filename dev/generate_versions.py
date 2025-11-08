from __future__ import annotations

import json
import logging

from flowforge.version import (
    get_latest_major_versions,
    get_latest_minor_versions,
    get_versions,
)

logger = logging.getLogger(__name__)


def get_package_versions() -> dict[str, list[str]]:
    r"""Get the versions for each package.

    Returns:
        A dictionary with the versions for each package.
    """
    return {
        "coola": list(get_versions("coola", lower="0.9.1", upper="1.0.0")),
        "packaging": list(get_latest_major_versions("packaging", lower="23.0")),
        "requests": list(get_latest_minor_versions("requests", lower="2.30.0", upper="3.0.0")),
    }


def main() -> None:
    logger.info(get_package_versions())
    logger.info(json.dumps(get_package_versions()))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
