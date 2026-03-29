"""Pytest configuration for test suite."""

from pathlib import Path
import sys
import time
import logging
import pytest
import allure

# Ensure project root is on sys.path so imports like `from utils.api_client` work
PROJECT_ROOT = Path(__file__).resolve().parent.parent
project_root_str = str(PROJECT_ROOT)

if project_root_str not in sys.path:
    sys.path.insert(0, project_root_str)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)


@pytest.fixture(autouse=True)
def log_test_timing(request):
    start = time.perf_counter()
    wall_start = time.strftime("%Y-%m-%d %H:%M:%S")
    logging.info("START %s at %s", request.node.nodeid, wall_start)
    yield
    duration = time.perf_counter() - start
    logging.info("END %s duration=%.3fs", request.node.nodeid, duration)
    try:
        allure.attach(
            f"{duration:.3f}s",
            name="duration",
            attachment_type=allure.attachment_type.TEXT,
        )
    except Exception:
        # Allure might be disabled; ignore timing attachment failures.
        pass
