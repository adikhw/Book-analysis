<div align="center">

# 📚 Book Analysis

**Analisis data buku dari hasil scraping: cek kualitas, bersihkan, rangkum, dan visualisasikan.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

![Tests](https://img.shields.io/badge/tests-10%20passed-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/status-selesai-success?style=flat-square)
![Project](https://img.shields.io/badge/project-4%20of%2010-blue?style=flat-square)

</div>

---

## 📖 Tentang Project

Program ini membaca `books.csv` hasil scraper (Project 3), memeriksa kualitas datanya, membersihkannya, menghitung ringkasan statistik, lalu menyimpan grafik sebagai file PNG. Semuanya dijalankan lewat satu perintah di terminal.

Dibuat sebagai latihan dasar data science: membaca CSV ke DataFrame, cleaning, `groupby`, statistik, visualisasi, dan tes dengan pytest.

## ✨ Fitur

| | Fitur | Keterangan |
|---|---|---|
| 📥 | **Muat data** | Baca CSV, validasi file dan kolom wajib dengan pesan error yang jelas |
| 🔍 | **Cek kualitas** | Nilai kosong, duplikat `url`, `price` tidak valid, `rating` di luar 1-5 |
| 🧹 | **Cleaning** | Buang duplikat dan baris tidak valid, isi nilai bawaan, rapikan tipe data |
| 📊 | **Statistik** | Ringkasan harga, buku termahal, distribusi rating, ringkasan per kategori, korelasi |
| 📈 | **Grafik** | 3 grafik PNG: histogram harga, batang rating, batang kategori |
| 🧪 | **Tes** | 10 tes pytest dengan data buatan, tanpa internet dan tanpa `books.csv` asli |

## 🛠️ Teknologi

| Library | Fungsi |
|---|---|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | Bahasa pemrograman utama |
| ![pandas](https://img.shields.io/badge/-pandas-150458?logo=pandas&logoColor=white) | Baca CSV, DataFrame, cleaning, `groupby`, statistik |
| ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?logo=plotly&logoColor=white) | Membuat dan menyimpan grafik |
| ![pytest](https://img.shields.io/badge/-pytest-0A9EDC?logo=pytest&logoColor=white) | Menjalankan tes |

Library bawaan Python yang dipakai: `pathlib`, `logging`, `argparse`, `sys`.

## 🚀 Instalasi

```bash
# 1. Clone repo
git clone https://github.com/adikhw/Book-analysis.git
cd Book-analysis

# 2. Buat virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install library
pip install -r requirements.txt
```

Lalu salin `books.csv` dari Project 3 ke folder `data/`.

## ▶️ Cara Pakai

```bash
python main.py
```

Dengan argumen:

```bash
python main.py --input data/books.csv --out output --top 10
```

| Argumen | Default | Fungsi |
|---|---|---|
| `--input` | `data/books.csv` | Path file CSV masukan |
| `--out` | `output` | Folder keluaran (grafik masuk ke `<out>/charts/`) |
| `--top` | `10` | Jumlah buku termahal dan jumlah kategori di grafik |

> ⚠️ Kalau file tidak ada, kolom wajib hilang, atau data kosong setelah dibersihkan, program menampilkan pesan error dan keluar dengan kode `1`.

## 🖥️ Contoh Output

Tempel output terminal dari dataset asli di sini:

```
=== Price summary ===
min     ...
max     ...
mean    ...
median  ...
std     ...
```

## 🖼️ Grafik

Salin PNG dari `output/charts/` ke folder `docs/` supaya tampil di GitHub (folder `output/` diabaikan Git).

| Sebaran harga | Rating per buku | Kategori terbanyak |
|---|---|---|
| ![Price](docs/price_hist.png) | ![Rating](docs/rating_bar.png) | ![Category](docs/category_bar.png) |

## 🧪 Menjalankan Tes

```bash
pytest
```

| File tes | Yang diuji |
|---|---|
| `tests/test_cleaner.py` | Duplikat, `price` kosong, `category` kosong, rating di luar rentang, tipe akhir, `check_quality` |
| `tests/test_analysis.py` | `price_summary`, `by_category`, `rating_distribution` |
| `tests/test_charts.py` | `plot_price_hist` menghasilkan PNG yang tidak kosong |

## 📁 Struktur Project

```
Book-analysis/
├── main.py            # titik masuk dan CLI
├── loader.py          # baca CSV dan cek kolom wajib
├── cleaner.py         # cek kualitas dan bersihkan data
├── analysis.py        # hitung ringkasan statistik
├── charts.py          # buat dan simpan grafik PNG
├── config.py          # konstanta
├── tests/             # tes pytest
├── data/              # books.csv (masukan)
├── output/charts/     # grafik hasil program
├── docs/              # grafik untuk README
├── requirements.txt
├── pytest.ini
└── README.md
```

## 🧠 Yang Dipelajari

- Membaca dan memeriksa data tabel dengan pandas
- Cleaning: missing value, duplikat, dan konversi tipe data
- Ringkasan dengan `groupby` dan statistik dasar
- Membuat grafik dengan matplotlib tanpa membuka jendela
- Menulis tes pytest dengan data buatan
- Memakai `logging` dan `argparse`

## 🔗 Project Terkait

- **Project 3:** Web Scraper, sumber `books.csv`
- **Project 5:** Capstone, memakai hasil analisis ini sebagai referensi

---

<div align="center">

Dibuat sebagai bagian dari perjalanan belajar Python 🐍

</div>
