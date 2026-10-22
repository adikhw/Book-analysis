import pandas as pd


def price_summary(df):
    return {
        "min": round(float(df["price"].min()), 2),
        "max": round(float(df["price"].max()), 2),
        "mean": round(float(df["price"].mean()), 2),
        "median": round(float(df["price"].median()), 2),
        "std": round(float(df["price"].std()), 2),
    }


def top_expensive(df, n):
    return df.sort_values("price", ascending=False).head(n)[["title", "price", "category"]]


def rating_distribution(df):
    counts = df["rating"].value_counts()
    return counts.reindex(range(1, 6), fill_value=0).sort_index()


def by_category(df):
    summary = df.groupby("category").agg(
        count=("title", "count"),
        avg_price=("price", "mean"),
        avg_rating=("rating", "mean"),
    )
    summary = summary.round({"avg_price": 2, "avg_rating": 2})
    return summary.sort_values("count", ascending=False).reset_index()


def price_rating_correlation(df):
    return float(df["price"].corr(df["rating"]))
