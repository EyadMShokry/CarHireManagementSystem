from typing import Union
from pathlib import Path

import yaml

def load_yaml(file_path: Union[Path, str]) -> dict:
    """Loads a YAML file as a dictionary.

    Args:
        file_path: Path to logging configuration YAML file.

    Returns: Loaded configuration as a dictionary.
    """
    with open(file_path, "r") as f:
        config = yaml.safe_load(f.read())
    return config
