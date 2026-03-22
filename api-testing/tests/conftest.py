"""Pytest configuration for test suite."""

from pathlib import Path
import sys

# Ensure project root is on sys.path so imports like `from utils.api_client` work
PROJECT_ROOT = Path(__file__).resolve().parent.parent
project_root_str = str(PROJECT_ROOT)

if project_root_str not in sys.path:
    sys.path.insert(0, project_root_str)
