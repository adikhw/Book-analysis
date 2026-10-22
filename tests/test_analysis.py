import pandas as pd
import pytest

from analysis import by_category, price_summary, rating_distribution


@pytest.fixture
def small_df():
    return pd.DataFrame({
        "title": ["a", "b", "c", "d", "e"],
        "price": [10.0, 30.0, 20.0, 40.0, 50.0],
        "rating": [5, 3, 4, 2, 1],
        "category": ["Fiction", "Fiction", "Poetry", "Poetry", "Poetry"],
    })


def test_price_summary_matches_hand_calculation(small_df):
    result = price_summary(small_df)

    assert result["min"] == 10.0
    assert result["max"] == 50.0
    assert result["mean"] == 30.0      # (10+30+20+40+50) / 5
    assert result["median"] == 30.0


def test_by_category_counts_and_averages(small_df):
    result = by_category(small_df)

    # Poetry has more books, so it comes first
    assert list(result["category"]) == ["Poetry", "Fiction"]

    poetry = result[result["category"] == "Poetry"].iloc[0]
    assert poetry["count"] == 3
    assert poetry["avg_price"] == 36.67   # (20+40+50) / 3
    assert poetry["avg_rating"] == 2.33   # (4+2+1) / 3

    fiction = result[result["category"] == "Fiction"].iloc[0]
    assert fiction["count"] == 2
    assert fiction["avg_price"] == 20.0   # (10+30) / 2
    assert fiction["avg_rating"] == 4.0   # (5+3) / 2


def test_rating_distribution_always_has_five_ratings(small_df):
    small_df = small_df[small_df["rating"] != 5]   # no book with rating 5

    result = rating_distribution(small_df)

    assert list(result.index) == [1, 2, 3, 4, 5]
    assert result[5] == 0
    assert result.sum() == 4
