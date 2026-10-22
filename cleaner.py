import logging

import pandas as pd

from config import RATING_RANGE, UNKNOWN_CATEGORY


def check_quality(df):
    low, high = RATING_RANGE

    return {
        "rows": len(df),
        "missing": df.isna().sum().to_dict(),
        "duplicates": df["url"].duplicated().sum(),
        "bad_price": (df["price"].isna() | (df["price"] <= 0)).sum(),
        "bad_rating": (df["rating"].isna() | (df["rating"] < low) | (df["rating"] > high)).sum(),
    }


def clean_df(df):
    low, high = RATING_RANGE
    result = df.copy()
    rows_before = len(result)

    # Duplicates (keep the first one)
    result = result.drop_duplicates(subset="url", keep="first")
    dropped_duplicates = rows_before - len(result)

    # Convert to numbers; unreadable values become NaN
    result["price"] = pd.to_numeric(result["price"], errors="coerce")
    result["rating"] = pd.to_numeric(result["rating"], errors="coerce")

    # Drop rows with invalid price
    bad_price = result["price"].isna() | (result["price"] <= 0)
    dropped_price = int(bad_price.sum())
    result = result[~bad_price]

    # Drop rows with invalid rating
    bad_rating = result["rating"].isna() | (result["rating"] < low) | (result["rating"] > high)
    dropped_rating = int(bad_rating.sum())
    result = result[~bad_rating].copy()

    # Fill non-core columns with defaults (handle missing values BEFORE changing types)
    filled_category = int(result["category"].isna().sum())
    result["category"] = result["category"].fillna(UNKNOWN_CATEGORY)

    result["stock_count"] = pd.to_numeric(result["stock_count"], errors="coerce")
    filled_stock = int(result["stock_count"].isna().sum())
    result["stock_count"] = result["stock_count"].fillna(0)

    filled_in_stock = int(result["in_stock"].isna().sum())
    result["in_stock"] = result["in_stock"].fillna(False)

    # Final types
    result["rating"] = result["rating"].astype(int)
    result["stock_count"] = result["stock_count"].astype(int)
    result["in_stock"] = result["in_stock"].astype(bool)

    # Tidy up text and index
    result["title"] = result["title"].str.strip()
    result["category"] = result["category"].str.strip()
    result = result.reset_index(drop=True)

    logging.info("Cleaning done: %d rows before, %d rows after", rows_before, len(result))
    if dropped_duplicates:
        logging.warning("%d rows dropped: duplicate url", dropped_duplicates)
    if dropped_price:
        logging.warning("%d rows dropped: invalid price", dropped_price)
    if dropped_rating:
        logging.warning("%d rows dropped: invalid rating", dropped_rating)
    if filled_category:
        logging.warning("%d empty category filled with '%s'", filled_category, UNKNOWN_CATEGORY)
    if filled_stock:
        logging.warning("%d empty stock_count filled with 0", filled_stock)
    if filled_in_stock:
        logging.warning("%d empty in_stock filled with False", filled_in_stock)

    return result
