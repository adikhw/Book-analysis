from pathlib import Path

import pandas as pd

from config import REQUIRED_COLUMNS


def load_books(path):
    if not Path(path).exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path, encoding="utf-8")

    lost_column = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if lost_column:
        raise ValueError(f"Missing column: {lost_column}")

    return df