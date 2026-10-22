import argparse
import logging
import sys

from analysis import (
    by_category,
    price_rating_correlation,
    price_summary,
    rating_distribution,
    top_expensive,
)
from charts import plot_category_bar, plot_price_hist, plot_rating_bar
from cleaner import check_quality, clean_df
from config import INPUT_CSV, OUT_DIR, TOP_N
from loader import load_books


def parse_args():
    parser = argparse.ArgumentParser(description="Analyze books.csv from the scraper project")
    parser.add_argument("--input", default=INPUT_CSV, help="path to input CSV")
    parser.add_argument("--out", default=OUT_DIR, help="output folder")
    parser.add_argument("--top", type=int, default=TOP_N, help="top N books/categories")
    return parser.parse_args()


def print_section(title):
    print(f"\n=== {title} ===")


def main():
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.info("Starting analysis from %s", args.input)

    raw = load_books(args.input)
    issues = check_quality(raw)
    logging.info(
        "Quality check: %d rows, %d duplicates, missing values: %s",
        issues["rows"], issues["duplicates"], issues["missing"],
    )

    clean = clean_df(raw)
    if clean.empty:
        logging.error("No valid data left after cleaning")
        sys.exit(1)

    prices = price_summary(clean)
    expensive = top_expensive(clean, args.top)
    ratings = rating_distribution(clean)
    categories = by_category(clean)
    corr = price_rating_correlation(clean)

    print_section("Price summary")
    for key, value in prices.items():
        print(f"{key:<8}{value}")

    print_section(f"Top {args.top} most expensive books")
    print(expensive.to_string(index=False))

    print_section("Rating distribution")
    print(ratings.to_string())

    print_section("Summary per category")
    print(categories.to_string(index=False))

    print_section("Price vs rating correlation")
    print(f"{corr:.3f}")

    chart_dir = f"{args.out}/charts"
    plot_price_hist(clean, f"{chart_dir}/price_hist.png")
    plot_rating_bar(ratings, f"{chart_dir}/rating_bar.png")
    plot_category_bar(categories, f"{chart_dir}/category_bar.png", args.top)
    print(f"\nCharts saved to: {chart_dir}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped by user")
        sys.exit(130)
    except Exception as e:
        logging.error("Program failed: %s", e)
        sys.exit(1)
