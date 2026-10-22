from pathlib import Path

import pandas as pd

from charts import plot_price_hist


def test_plot_price_hist_creates_non_empty_png(tmp_path):
    df = pd.DataFrame({"price": [10.0, 20.0, 30.0, 40.0, 50.0]})
    path = tmp_path / "charts" / "price_hist.png"   # folder does not exist yet

    plot_price_hist(df, path)

    assert Path(path).exists()
    assert path.stat().st_size > 0
