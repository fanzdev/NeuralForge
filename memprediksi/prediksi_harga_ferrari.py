import pandas as pd
from sklearn.linear_model import LinearRegression

dataHargaFerrari = {
    "tahun": [2020, 2021, 2022, 2023, 2024, 2025, 2026],
    "harga": [200000, 220000, 250000, 300000, 350000, 400000, 420000]
}

default = pd.DataFrame(dataHargaFerrari)

prediksiHargaFerrari = default[["tahun"]]
prediksiHargaFerrariTarget = default["harga"]

model = LinearRegression()
model.fit(prediksiHargaFerrari, prediksiHargaFerrariTarget)

print("=====================================================")
print("| APLIKASI SEDERHANA - PREDIKSI HARGA MOBIL FERRARI |")
print("=====================================================")
inputTahun = int(input("> Masukkan Tahun Untuk di Prediksi: "))
print()

prediksiHarga = model.predict(pd.DataFrame({"tahun": [inputTahun]}))

print("> Prediksi Harga:", format(prediksiHarga[0], ",.2f"), "USD")
print("=====================================================")
print("|                 ACH. AFANOR RIDHA                 |")
print("=====================================================")