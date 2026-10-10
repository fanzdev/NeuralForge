## Mengimpor library pandas untuk mengolah data dalam bentuk tabel
import pandas as pd

# Mengimpor LinearRegression untuk membuat model regresi linear
from sklearn.linear_model import LinearRegression

# Data
# Membuat dataset berisi luas tanah dan harga tanah
dataTanah = {
    "luas_tanah": [50, 75, 100, 125, 150, 175, 200],  # Data luas tanah dalam m²
    "harga": [100, 150, 200, 250, 300, 400, 450]     # Harga tanah dalam juta rupiah
}

# Mengubah dictionary menjadi DataFrame (tabel data) menggunakan pandas
default = pd.DataFrame(dataTanah)

# Input dan Target
# X (fitur/input): data yang digunakan untuk memprediksi, yaitu luas tanah
x = default[["luas_tanah"]]

# Y (target/output): nilai yang ingin diprediksi, yaitu harga tanah
y = default["harga"]

# Membuat Model
# Membuat objek model Linear Regression
model = LinearRegression()

# Melatih model menggunakan data luas tanah (x) dan harga tanah (y)
# Model akan mempelajari hubungan antara luas tanah dan harga tanah
model.fit(x, y)

# Menentukan luas tanah baru yang ingin diprediksi harganya, yaitu 175 m²
tanahBaru = [[400]]

# Menggunakan model yang sudah dilatih untuk memprediksi harga tanah baru
prediksi = model.predict(tanahBaru)

# Hasil
# Menampilkan luas tanah yang ingin diprediksi
print("Luas tanah:", tanahBaru[0][0], "m2")

# Menampilkan hasil prediksi harga tanah dalam juta rupiah
print("Prediksi Harga:", prediksi[0], "Juta Rupiah")