from pathlib import Path

import matplotlib.pyplot as plt


def plot_price_hist(df, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.hist(df["price"], bins=20, edgecolor="black")
    plt.title("Book Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Number of books")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def plot_rating_bar(dist, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.bar(dist.index, dist.values, edgecolor="black")
    plt.xticks(list(dist.index))
    plt.title("Number of Books per Rating")
    plt.xlabel("Rating")
    plt.ylabel("Number of books")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def plot_category_bar(cat_df, path, n):
    top = cat_df.head(n)
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 6))
    plt.barh(top["category"], top["count"], edgecolor="black")
    plt.gca().invert_yaxis()  # biggest category on top
    plt.title(f"Top {len(top)} Categories by Number of Books")
    plt.xlabel("Number of books")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
