import pandas as pd
import pytest

from cleaner import check_quality, clean_df


@pytest.fixture
def dirty_df():
    return pd.DataFrame({
        "title": ["A", "B", "C", "A again", "E", "F", "G"],
        "price": [10.0, 20.0, 30.0, 10.0, None, 15.0, 25.0],
        "rating": [3, 4, 5, 3, 4, 7, 2],
        "category": ["Fiction", "Poetry", "Fiction", "Fiction", "Poetry", "Poetry", None],
        "in_stock": [True, True, False, True, True, True, True],
        "stock_count": [5, 3, 0, 5, 2, 1, None],
        "url": ["u1", "u2", "u3", "u1", "u4", "u5", "u6"],
    })


def test_clean_df_drops_duplicate_url(dirty_df):
    result = clean_df(dirty_df)

    assert result["url"].is_unique
    assert "A again" not in result["title"].values


def test_clean_df_drops_missing_price(dirty_df):
    result = clean_df(dirty_df)

    assert "E" not in result["title"].values
    assert result["price"].notna().all()


def test_clean_df_fills_empty_category_without_dropping_row(dirty_df):
    result = clean_df(dirty_df)

    row = result[result["title"] == "G"]
    assert len(row) == 1
    assert row["category"].iloc[0] == "Unknown"
    assert row["stock_count"].iloc[0] == 0


def test_clean_df_drops_rating_out_of_range(dirty_df):
    result = clean_df(dirty_df)

    assert "F" not in result["title"].values
    # 7 rows -> 1 duplicate, 1 empty price, 1 rating 7 dropped -> 4 left
    assert len(result) == 4


def test_clean_df_final_types_and_original_untouched(dirty_df):
    original = dirty_df.copy()
    result = clean_df(dirty_df)

    assert pd.api.types.is_integer_dtype(result["rating"])
    assert pd.api.types.is_integer_dtype(result["stock_count"])
    assert pd.api.types.is_bool_dtype(result["in_stock"])
    pd.testing.assert_frame_equal(dirty_df, original)


def test_check_quality_counts_problems(dirty_df):
    report = check_quality(dirty_df)

    assert report["rows"] == 7
    assert report["duplicates"] == 1
    assert report["bad_price"] == 1
    assert report["bad_rating"] == 1
