<div align="center">

# 🧠 NeuralForge

### Laboratorium Machine Learning Pribadi

**Dari data mentah menjadi wawasan — satu eksperimen dalam satu waktu.**

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Focus-Machine%20Learning-7C3AED?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Learning-22C55E?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python-0EA5E9?style=for-the-badge&logo=python&logoColor=white)

*Repository untuk menyimpan proses belajar, latihan, eksperimen, project pribadi, dan tugas kuliah di bidang Machine Learning.*

</div>

---

## 📖 Tentang NeuralForge

**NeuralForge** adalah repository pribadi untuk mempelajari, menguji, dan membangun project **Machine Learning (ML)** menggunakan Python.

Repository ini menjadi tempat dokumentasi perjalanan belajar saya, mulai dari dasar Python dan pengolahan data hingga pemodelan, evaluasi, dan eksperimen ML yang lebih kompleks.

Isi repository dapat mencakup:
- Latihan Python untuk pengolahan data.
- Eksplorasi dan visualisasi dataset.
- Prediksi menggunakan algoritma regresi.
- Klasifikasi data.
- Clustering dan pembelajaran tanpa label.
- Evaluasi serta perbandingan model.
- Eksperimen algoritma dan parameter.
- Project pribadi dan tugas akademik.
- Catatan konsep, kesalahan, dan hal yang dipelajari.

Repository ini akan berkembang secara bertahap. Tidak semua folder, library, atau topik yang tercantum di bawah harus sudah tersedia atau sudah dikuasai.

> **Prinsip:** Pahami masalahnya, periksa datanya, bangun modelnya, evaluasi hasilnya, lalu dokumentasikan pelajarannya.

## 🎯 Tujuan

1. Memperkuat dasar Python untuk analisis data dan ML.
2. Memahami NumPy, Pandas, serta visualisasi data.
3. Belajar membersihkan dan menyiapkan dataset.
4. Memahami supervised learning dan unsupervised learning.
5. Mencoba regresi, klasifikasi, dan clustering.
6. Memahami train-test split, validasi, dan metrik evaluasi.
7. Membuat project yang mudah dijalankan ulang.
8. Menyimpan tugas dan eksperimen secara terstruktur.
9. Membangun portofolio Machine Learning yang terus berkembang.

## 🧰 Teknologi dan library

Library yang digunakan bergantung pada kebutuhan masing-masing project.

| Library / modul | Kegunaan |
|---|---|
| `numpy` | Operasi numerik, array, dan perhitungan matematika |
| `pandas` | Membaca, membersihkan, mengolah, dan menganalisis data berbentuk tabel |
| `matplotlib` | Membuat grafik dan visualisasi |
| `seaborn` | Visualisasi statistik |
| `scikit-learn` | Algoritma ML klasik, preprocessing, pipeline, dan evaluasi |
| `sklearn.linear_model` | Modul model linear seperti regresi linear dan logistic regression |
| `LinearRegression` | Kelas model regresi linear dari `sklearn.linear_model` |
| `train_test_split` | Membagi dataset menjadi data latih dan data uji |
| `mean_absolute_error`, `mean_squared_error`, `r2_score` | Metrik evaluasi regresi |
| `accuracy_score`, `classification_report`, `confusion_matrix` | Evaluasi model klasifikasi |
| `Jupyter` / `ipykernel` | Menjalankan notebook interaktif |
| `joblib` | Menyimpan dan memuat model Python/Scikit-learn |
| `SciPy` | Komputasi ilmiah dan matematika |
| `statsmodels` | Analisis statistik dan model statistik |
| `plotly` | Visualisasi data interaktif |
| `imbalanced-learn` | Teknik untuk menangani dataset dengan kelas tidak seimbang |
| `xgboost`, `lightgbm`, `catboost` | Algoritma gradient boosting |
| `Pillow` | Pemrosesan gambar dasar |
| `opencv-python` | Pengolahan citra komputer |
| `torch` | Deep learning dengan PyTorch |
| `tensorflow` / `keras` | Deep learning dan neural network |
| `transformers` | Model machine learning dan AI dari ekosistem Hugging Face |

**Catatan penting:** `LinearRegression` bukan library terpisah. Ia adalah sebuah **kelas** yang diimpor dari modul `sklearn.linear_model`, sedangkan nama paket yang dipasang melalui `pip` adalah **`scikit-learn`**.

Contoh impor:

```python
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

---

# ⚙️ Instalasi dan Persiapan Lingkungan

Panduan berikut terutama ditujukan untuk **Windows 10/11 menggunakan VS Code dan terminal CMD atau PowerShell**. Perintah Linux/macOS juga disertakan pada bagian aktivasi lingkungan.

## 1. Persyaratan awal

Siapkan perangkat lunak berikut:

- **Python 3** — unduh dari [python.org](https://www.python.org/downloads/).
- **Visual Studio Code** — unduh dari [code.visualstudio.com](https://code.visualstudio.com/).
- **Git** — opsional, tetapi disarankan untuk mengelola repository GitHub.
- Koneksi internet untuk mengunduh package.

Saat menginstal Python di Windows, aktifkan opsi **Add Python to PATH** jika tersedia.

Periksa apakah Python dan pip sudah dapat digunakan:

```bash
python --version
python -m pip --version
```

Jika perintah `python` tidak dikenali, coba:

```bash
py --version
py -m pip --version
```

Jika keduanya tidak berjalan, periksa kembali instalasi Python dan PATH. Tutup lalu buka terminal baru setelah melakukan perubahan PATH.

## 2. Clone repository atau buka folder project

Jika repository sudah tersedia di GitHub:

```bash
git clone https://github.com/USERNAME/neural-forge.git
cd neural-forge
```

Ganti `USERNAME` dengan username GitHub milikmu.

Jika belum mengunggah repository, buat folder project sendiri terlebih dahulu:

```bash
mkdir neural-forge
cd neural-forge
```

Buka folder tersebut di VS Code:

```bash
code .
```

Jika perintah `code` belum tersedia, buka VS Code secara manual lalu pilih **File → Open Folder**.

## 3. Membuat virtual environment `.venv`

Virtual environment memisahkan library project ini dari instalasi Python global atau project lain. Dengan begitu, dependency setiap project lebih mudah dikelola.

Jalankan dari direktori utama project:

```bash
python -m venv .venv
```

Jika perintah `python` tidak tersedia tetapi `py` berfungsi:

```bash
py -m venv .venv
```

Setelah berhasil, akan muncul folder `.venv/`. Folder ini berisi lingkungan Python khusus project.

## 4. Mengaktifkan `.venv`

Aktivasi dilakukan **setiap kali membuka terminal baru** sebelum menjalankan project atau memasang package.

### Windows — Command Prompt (CMD)

```bat
.venv\Scripts\activate.bat
```

### Windows — PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Jika PowerShell menolak menjalankan script karena kebijakan eksekusi, kamu dapat memakai aktivasi melalui CMD atau membaca kebijakan eksekusi PowerShell di dokumentasi resmi Microsoft. Jangan mengubah kebijakan keamanan secara luas tanpa memahami dampaknya.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Memastikan `.venv` aktif

Biasanya nama `(.venv)` muncul di awal baris terminal. Periksa interpreter dan lokasi Python yang sedang digunakan:

```bash
python --version
python -m pip --version
```

Di Windows, pemeriksaan tambahan:

```bat
where python
```

Path Python yang aktif seharusnya mengarah ke folder `.venv`.

### Menonaktifkan `.venv`

```bash
deactivate
```

Perintah ini menonaktifkan virtual environment pada terminal tersebut. File dan library yang sudah terpasang di `.venv` tidak otomatis dihapus.

## 5. Memperbarui pip

Pastikan `.venv` aktif, lalu jalankan:

```bash
python -m pip install --upgrade pip setuptools wheel
```

Menggunakan `python -m pip` membantu memastikan package dipasang melalui interpreter Python yang sedang aktif.

---

# 📦 Instalasi Library Machine Learning

**Penting:** Jangan memasang semua library ML sekaligus tanpa kebutuhan. Beberapa package deep learning berukuran besar, membutuhkan versi Python tertentu, atau memiliki persyaratan perangkat keras khusus. Mulailah dari paket dasar, lalu tambahkan library sesuai project.

## A. Paket dasar yang disarankan

Untuk belajar Python, pengolahan data, visualisasi, regresi, klasifikasi, dan algoritma ML klasik:

```bash
python -m pip install numpy pandas matplotlib seaborn scikit-learn jupyter ipykernel
```

Paket tambahan yang sering berguna:

```bash
python -m pip install scipy statsmodels joblib openpyxl
```

Kegunaan `openpyxl`: membaca atau menulis file Excel `.xlsx` melalui Pandas.

## B. Notebook dan eksplorasi data

Untuk menjalankan Jupyter Notebook:

```bash
python -m pip install notebook
jupyter notebook
```

Atau untuk JupyterLab:

```bash
python -m pip install jupyterlab
jupyter lab
```

Pilih salah satu antarmuka sesuai kebutuhan. Untuk mendaftarkan `.venv` sebagai kernel notebook:

```bash
python -m ipykernel install --user --name neural-forge --display-name "Python (NeuralForge)"
```

Di Jupyter, pilih kernel **Python (NeuralForge)** agar notebook memakai interpreter project yang benar.

## C. Import yang umum digunakan

### NumPy dan Pandas

```python
import numpy as np
import pandas as pd
```

Contoh membaca CSV:

```python
data = pd.read_csv("data.csv")
print(data.head())
print(data.info())
print(data.describe())
```

### Visualisasi

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

Contoh grafik sederhana:

```python
data["harga"].plot(kind="hist", title="Distribusi Harga")
plt.xlabel("Harga")
plt.show()
```

Pastikan kolom `harga` benar-benar ada di dataset yang digunakan.

### Regresi linear dengan Scikit-learn

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

Contoh alur dasar (sesuaikan nama kolom dan dataset):

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Dataset harus memiliki kolom "luas_tanah" dan "harga".
data = pd.read_csv("data_tanah.csv")

X = data[["luas_tanah"]]
y = data["harga"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

prediksi = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, prediksi))
print("MSE:", mean_squared_error(y_test, prediksi))
print("R²:", r2_score(y_test, prediksi))
```

`X` adalah fitur atau input model, sedangkan `y` adalah target yang ingin dipelajari atau diprediksi. Contoh di atas hanya berlaku jika dataset memiliki kolom yang sesuai dan cukup data yang valid.

### Modul Scikit-learn yang sering dipakai

| Modul / kelas / fungsi | Kegunaan |
|---|---|
| `sklearn.linear_model.LinearRegression` | Regresi linear |
| `sklearn.linear_model.Ridge` | Regresi linear dengan regularisasi L2 |
| `sklearn.linear_model.Lasso` | Regresi linear dengan regularisasi L1 |
| `sklearn.linear_model.LogisticRegression` | Klasifikasi dengan logistic regression |
| `sklearn.tree.DecisionTreeRegressor` | Regresi dengan decision tree |
| `sklearn.tree.DecisionTreeClassifier` | Klasifikasi dengan decision tree |
| `sklearn.ensemble.RandomForestRegressor` | Regresi menggunakan random forest |
| `sklearn.ensemble.RandomForestClassifier` | Klasifikasi menggunakan random forest |
| `sklearn.ensemble.GradientBoostingRegressor` | Regresi dengan gradient boosting |
| `sklearn.neighbors.KNeighborsClassifier` | Klasifikasi K-nearest neighbors |
| `sklearn.cluster.KMeans` | Clustering K-means |
| `sklearn.preprocessing.StandardScaler` | Standardisasi fitur |
| `sklearn.preprocessing.MinMaxScaler` | Mengubah skala fitur |
| `sklearn.preprocessing.OneHotEncoder` | Mengubah kategori menjadi fitur numerik |
| `sklearn.impute.SimpleImputer` | Menangani nilai yang hilang |
| `sklearn.model_selection.train_test_split` | Membagi data latih dan data uji |
| `sklearn.model_selection.cross_val_score` | Evaluasi dengan cross-validation |
| `sklearn.pipeline.Pipeline` | Menyatukan preprocessing dan model dalam pipeline |
| `sklearn.metrics.mean_absolute_error` | Mengukur rata-rata kesalahan absolut regresi |
| `sklearn.metrics.mean_squared_error` | Mengukur rata-rata kesalahan kuadrat regresi |
| `sklearn.metrics.r2_score` | Metrik R² untuk regresi |
| `sklearn.metrics.accuracy_score` | Akurasi klasifikasi |
| `sklearn.metrics.classification_report` | Precision, recall, dan F1-score |
| `sklearn.metrics.confusion_matrix` | Matriks hasil klasifikasi |

Semua kelas dan fungsi di tabel tersebut tersedia melalui paket **`scikit-learn`**. Kamu tidak perlu memasangnya satu per satu.

## D. Paket analisis dan visualisasi tambahan

```bash
python -m pip install plotly missingno yellowbrick
```

- `plotly`: grafik interaktif.
- `missingno`: visualisasi nilai yang hilang.
- `yellowbrick`: visualisasi diagnostik model ML.

Paket tambahan lain untuk kebutuhan tertentu:

```bash
python -m pip install imbalanced-learn
python -m pip install xgboost
python -m pip install lightgbm
python -m pip install catboost
```

- `imbalanced-learn`: teknik menangani distribusi kelas yang tidak seimbang.
- `xgboost`, `lightgbm`, `catboost`: algoritma gradient boosting.

Instal secara terpisah bila diperlukan agar lebih mudah menemukan sumber error instalasi.

## E. Deep learning — opsional

Deep learning tidak diperlukan untuk memulai regresi linear atau ML klasik.

### PyTorch

Ikuti pemilih instalasi resmi agar perintah sesuai dengan sistem operasi dan kebutuhan CPU/GPU:

https://pytorch.org/get-started/locally/

Setelah instalasi, uji:

```bash
python -c "import torch; print(torch.__version__)"
```

### TensorFlow / Keras

Periksa dukungan versi Python dan perangkat keras pada dokumentasi resmi:

https://www.tensorflow.org/install

Instalasi umum, jika versi Python dan sistemmu didukung:

```bash
python -m pip install tensorflow
```

Uji:

```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

### Hugging Face Transformers

Untuk eksperimen model bahasa dan model pretrained:

```bash
python -m pip install transformers
```

Banyak workflow Transformers juga memerlukan backend seperti PyTorch, serta bisa membutuhkan ruang penyimpanan dan memori yang besar.

## F. Computer vision dan pemrosesan gambar — opsional

```bash
python -m pip install pillow opencv-python
```

- `Pillow`: membaca, mengubah ukuran, dan memproses gambar.
- `opencv-python`: computer vision dan pemrosesan citra.

Untuk project headless/server, varian OpenCV yang dipilih bisa berbeda. Jangan memasang beberapa varian OpenCV sekaligus kecuali memang memahami konflik dependensinya.

## G. Membaca berbagai format data

```bash
python -m pip install openpyxl
python -m pip install pyarrow
python -m pip install xlrd
```

- `openpyxl`: file Excel `.xlsx`.
- `pyarrow`: format kolom seperti Parquet dan integrasi data tertentu.
- `xlrd`: membaca format Excel lama `.xls` pada versi dan format yang didukung.

Untuk file CSV, Pandas biasanya sudah cukup tanpa library tambahan.

## H. Utilitas project

```bash
python -m pip install python-dotenv tqdm requests pyyaml
```

- `python-dotenv`: membaca konfigurasi dari file `.env`.
- `tqdm`: progress bar.
- `requests`: HTTP request ke API.
- `PyYAML`: membaca file konfigurasi YAML.

Jangan commit file `.env` yang berisi token, password, atau API key ke GitHub.

---

# ▶️ Menjalankan Project Python

## 1. Pastikan terminal berada di folder project

Contoh:

```bash
cd neural-forge
```

## 2. Aktifkan virtual environment

Windows CMD:

```bat
.venv\Scripts\activate.bat
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 3. Jalankan file Python

Misalnya struktur project:

```text
neural-forge/
└── experiments/
    └── prediksi_harga/
        └── main.py
```

Dari folder utama repository, jalankan:

```bash
python experiments/prediksi_harga/main.py
```

Atau masuk ke folder project:

```bash
cd experiments/prediksi_harga
python main.py
```

Nama file dan path harus sesuai dengan file yang benar-benar ada.

## 4. Menjalankan Jupyter Notebook

Pastikan `.venv` aktif dan Jupyter sudah terpasang:

```bash
jupyter notebook
```

Bila perintah `jupyter` tidak ditemukan, coba:

```bash
python -m notebook
```

## 5. Memilih interpreter Python di VS Code

1. Buka folder repository di VS Code.
2. Pastikan ekstensi **Python** dari Microsoft sudah terpasang.
3. Tekan `Ctrl + Shift + P`.
4. Cari **Python: Select Interpreter**.
5. Pilih interpreter di `.venv`, biasanya `.venv\Scripts\python.exe` pada Windows.
6. Buka terminal baru dan aktifkan `.venv` jika belum aktif.
7. Jalankan file menggunakan terminal untuk memastikan interpreter yang digunakan benar.

VS Code terkadang mengaktifkan environment otomatis, tetapi tetap periksa terminal dan interpreter yang dipilih.

---

# 📋 Mengelola Dependency

## 1. Melihat package yang terpasang

```bash
python -m pip list
```

Melihat informasi satu package:

```bash
python -m pip show pandas
python -m pip show scikit-learn
```

Memeriksa konflik dependency:

```bash
python -m pip check
```

## 2. Menyimpan dependency ke `requirements.txt`

Setelah project berjalan dan dependency sudah sesuai:

```bash
python -m pip freeze > requirements.txt
```

Perintah tersebut mencatat seluruh package yang terpasang di environment aktif, termasuk dependency transitive. Karena itu, jalankan di `.venv` project yang benar, bukan di Python global.

Untuk project yang lebih besar, pertimbangkan menyusun dependency langsung secara sengaja agar file lebih mudah dirawat.

## 3. Menginstal dependency dari `requirements.txt`

Di komputer baru atau environment baru:

```bash
python -m venv .venv
```

Aktifkan `.venv`, lalu:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 4. Memasang package baru

Contoh:

```bash
python -m pip install pandas
```

Setelah package ditambahkan, perbarui `requirements.txt` jika package tersebut memang dibutuhkan untuk project.

## 5. Menghapus package

```bash
python -m pip uninstall nama-package
```

Ganti `nama-package` dengan nama package yang ingin dihapus, misalnya `seaborn`.

## 6. Menghapus dan membuat ulang `.venv`

Jika environment rusak, kamu dapat membuat ulangnya. Pastikan tidak ada proses Python yang sedang menggunakan environment tersebut.

Windows CMD:

```bat
deactivate
rmdir /s /q .venv
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

PowerShell:

```powershell
deactivate
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Menghapus `.venv` tidak menghapus kode project, tetapi semua package yang hanya terpasang di environment tersebut perlu dipasang ulang.

---

# 🗂️ Struktur Repository yang Disarankan

Struktur berikut adalah contoh yang bisa dikembangkan. Tidak harus dibuat sekaligus.

```text
neural-forge/
├── fundamentals/
│   ├── python-basics/
│   └── ml-introduction/
├── data-analysis/
│   ├── data-cleaning/
│   └── exploratory-data-analysis/
├── supervised-learning/
│   ├── regression/
│   └── classification/
├── unsupervised-learning/
│   └── clustering/
├── model-evaluation/
├── experiments/
├── college-projects/
├── applied-projects/
├── notes/
├── .gitignore
├── requirements.txt
└── README.md
```

Setiap project yang cukup besar sebaiknya memiliki dokumentasi sendiri, misalnya:

```text
prediksi-harga-tanah/
├── data/
│   └── README.md
├── notebooks/
│   └── exploration.ipynb
├── src/
│   └── main.py
├── requirements.txt
└── README.md
```

Hindari mengunggah dataset besar, data pribadi, file sementara, atau model berukuran besar tanpa mempertimbangkan ukuran repository dan izin distribusinya.

## 🧹 Contoh `.gitignore`

Buat file bernama `.gitignore` di direktori utama agar file lokal dan file sensitif tidak ikut diunggah:

```gitignore
# Virtual environment
.venv/
venv/
env/

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Environment variables / secrets
.env
.env.*
!.env.example

# Jupyter
.ipynb_checkpoints/

# Editor
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

# Logs
*.log

# Local data (aktifkan bila dataset tidak boleh diunggah)
# data/private/
# data/raw/
```

Periksa aturan `.gitignore` sebelum mengunggah. Jika dataset boleh dibagikan dan ukurannya wajar, dokumentasikan sumber serta lisensinya. File yang sudah terlanjur dilacak Git tidak otomatis berhenti dilacak hanya karena ditambahkan ke `.gitignore`.

---

# 🧪 Alur Kerja Machine Learning

1. **Tentukan masalah** — apa yang ingin dijawab atau diprediksi?
2. **Pahami dataset** — periksa jumlah baris, kolom, tipe data, nilai kosong, dan duplikasi.
3. **Eksplorasi data (EDA)** — cari pola, distribusi, dan kemungkinan anomali.
4. **Siapkan fitur dan target** — pisahkan input `X` dan target `y`.
5. **Bagi data dengan benar** — pisahkan data latih dan data uji; hindari kebocoran data.
6. **Buat baseline** — mulai dari model sederhana sebagai pembanding.
7. **Latih model** — gunakan algoritma yang sesuai dengan jenis masalah.
8. **Evaluasi** — gunakan metrik yang relevan, bukan hanya satu skor.
9. **Analisis kesalahan** — periksa kondisi saat model memberikan hasil yang buruk.
10. **Dokumentasikan** — catat sumber data, metode, hasil, keterbatasan, dan cara menjalankan project.

Hasil model tidak otomatis benar hanya karena metriknya tinggi. Kualitas data, pemisahan data yang tepat, validasi, dan konteks penggunaan harus tetap diperhatikan.

# 📊 Checklist Belajar

- [ ] Memahami dasar Python.
- [ ] Memahami variabel, kondisi, perulangan, fungsi, dan struktur data.
- [ ] Memahami NumPy.
- [ ] Memahami Pandas dan membaca file CSV.
- [ ] Melakukan data cleaning dan EDA.
- [ ] Membuat visualisasi data.
- [ ] Memahami fitur (`X`) dan target (`y`).
- [ ] Memahami train-test split.
- [ ] Membuat model `LinearRegression`.
- [ ] Memahami MAE, MSE, dan R².
- [ ] Belajar classification dan metriknya.
- [ ] Belajar preprocessing dan pipeline.
- [ ] Mencoba clustering.
- [ ] Menyelesaikan project end-to-end.
- [ ] Menulis dokumentasi yang dapat diikuti orang lain.

Perbarui checklist sesuai progres nyata. Tidak perlu mencentang topik yang belum dipelajari.

# 🛠️ Troubleshooting

### `python is not recognized`

Python mungkin belum terpasang atau belum ditambahkan ke PATH. Coba `py --version`, periksa instalasi Python, lalu buka terminal baru.

### `No module named 'pandas'`

Kemungkinan package dipasang di interpreter yang berbeda. Aktifkan `.venv`, lalu:

```bash
python -m pip install pandas
```

Periksa juga interpreter yang dipilih di VS Code.

### Aktivasi PowerShell ditolak

Coba aktivasi dari CMD:

```bat
.venv\Scripts\activate.bat
```

Atau gunakan panduan resmi Microsoft untuk memahami execution policy. Jangan menonaktifkan perlindungan sistem secara global hanya demi aktivasi environment.

### `pip` tidak ditemukan

Gunakan:

```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

Jika Python memiliki instalasi yang bermasalah, perbaiki instalasinya dari sumber resmi.

### Instalasi package gagal

- Pastikan koneksi internet berjalan.
- Pastikan `.venv` aktif.
- Periksa versi Python dan kompatibilitas package.
- Baca pesan error lengkap, terutama baris terakhir.
- Coba upgrade pip.
- Untuk TensorFlow, PyTorch, LightGBM, dan package khusus lainnya, ikuti petunjuk instalasi resmi masing-masing.

### File atau dataset tidak ditemukan

Path relatif dihitung dari direktori kerja saat program dijalankan. Pastikan terminal berada di folder yang benar dan nama file sesuai, termasuk ekstensi serta huruf besar-kecil pada sistem yang membedakannya.

---

# 🔐 Data, Etika, dan Keamanan

- Hormati lisensi dataset dan package pihak ketiga.
- Jangan mengunggah API key, token, password, atau data rahasia.
- Jangan mengunggah data pribadi tanpa izin yang sesuai.
- Jelaskan keterbatasan dataset dan model.
- Hindari klaim yang tidak didukung hasil eksperimen.
- Untuk tugas akademik, ikuti aturan institusi dan cantumkan referensi atau kolaborator sesuai ketentuan.

# 🤝 Kontribusi dan Masukan

Repository ini terutama merupakan ruang belajar dan portofolio pribadi. Masukan yang membangun, koreksi, dan saran pengembangan sangat dihargai. Jika fitur Issues atau Discussions diaktifkan, kamu dapat menggunakannya untuk berdiskusi atau melaporkan masalah.

# 📜 Lisensi

Lisensi repository perlu ditetapkan secara eksplisit. Jika memilih MIT, tambahkan file `LICENSE` yang berisi teks lisensi MIT yang benar. Jangan menganggap semua dataset, notebook, atau materi pihak ketiga otomatis tercakup oleh lisensi repository ini.

---

<div align="center">

### ⚡ Explore. Experiment. Evaluate. Evolve.

**NeuralForge — membangun pemahaman melalui Machine Learning.**

<sub>Repository pembelajaran dan portofolio yang terus berkembang.</sub>

</div>
