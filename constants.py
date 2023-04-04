"""Project Constants."""

from pathlib import Path

# Root directory for the Project.
PROJECT_ROOT_DIR = Path(__file__).parent

# Configuration file in configuration directory under project root directory.
DB_CONNECTION_CONFIGURATION_FILE_PATH = str(
    Path(PROJECT_ROOT_DIR, "configurations/db_connection.yaml")
)
