# Aplikasi Cuaca PyQt5

Aplikasi cuaca sederhana yang dibuat dengan menggunakan PyQt5 dan API dari OpenWeatherMap. Aplikasi ini memungkinkan pengguna untuk memasukkan nama kota dan menampilkan suhu, ikon cuaca, serta deskripsi cuaca berdasarkan data yang diambil dari OpenWeatherMap.

## Fitur
- Input kota dari pengguna.
- Menampilkan suhu dalam derajat Celcius.
- Menampilkan ikon cuaca berdasarkan kondisi cuaca saat ini.
- Menampilkan deskripsi cuaca.

## Prasyarat

Pastikan Anda sudah menginstal **Python 3.x** di sistem Anda. Anda juga perlu API key dari [OpenWeatherMap](https://openweathermap.org/api). 

### Dependensi

Untuk menjalankan aplikasi ini, Anda perlu menginstal beberapa paket Python berikut:

- **PyQt5** untuk UI
- **Requests** untuk mengambil data dari API cuaca

Anda bisa menginstalnya dengan menjalankan perintah berikut:

```bash
pip install PyQt5 requests
```

## Instalasi

1. Clone repository ini:

    ```bash
    git clone https://github.com/username/repo-name.git
    ```

2. Masuk ke direktori proyek:

    ```bash
    cd repo-name
    ```

3. Instal semua dependensi yang dibutuhkan:

    ```bash
    pip install -r requirements.txt
    ```

4. Dapatkan API key dari [OpenWeatherMap](https://openweathermap.org/api) dan ganti `YOUR_API_KEY` di dalam file `weather_app_styled.py` dengan API key Anda.

## Cara Menjalankan

1. Setelah mengatur API key, jalankan aplikasi dengan perintah berikut:

    ```bash
    python weather_app_styled.py
    ```

2. Masukkan nama kota yang ingin Anda cari di dalam aplikasi, kemudian tekan tombol "Get Weather" untuk melihat kondisi cuaca saat ini.
