import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# OpenWeatherMap untuk mendapatkan data cuaca
API_KEY = 'dcfff4717ca150a56d93982ee6d81b9a'  # Ganti dengan API key OpenWeatherMap Anda

def get_weather(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return None

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aplikasi Cuaca PyQt5")
        self.setGeometry(300, 300, 400, 350)

        # Widget utama dan layout vertikal
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        # Label untuk nama kota
        self.city_label = QLabel("Nama Kota:", self)
        layout.addWidget(self.city_label)

        # Input untuk nama kota
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Masukkan nama kota")
        layout.addWidget(self.city_input)

        # Tombol untuk mendapatkan cuaca
        self.weather_button = QPushButton("Get Weather", self)
        self.weather_button.clicked.connect(self.on_get_weather)
        layout.addWidget(self.weather_button)

        # Label untuk menampilkan suhu
        self.temperature_label = QLabel("Suhu: -", self)
        layout.addWidget(self.temperature_label)

        # Label untuk menampilkan emoji cuaca
        self.weather_icon_label = QLabel(self)
        layout.addWidget(self.weather_icon_label)

        # Label untuk menampilkan deskripsi cuaca
        self.description_label = QLabel("Deskripsi: -", self)
        layout.addWidget(self.description_label)

        # Set layout ke widget utama
        self.central_widget.setLayout(layout)

        # Tambahkan styling menggunakan QSS
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }
            QLabel {
                font-size: 16px;
                color: #333;
            }
            QLineEdit {
                font-size: 14px;
                padding: 5px;
                border: 1px solid #bbb;
                border-radius: 5px;
            }
            QPushButton {
                font-size: 14px;
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QLabel#temperature_label {
                font-size: 20px;
                font-weight: bold;
                color: #007BFF;
            }
            QLabel#description_label {
                font-style: italic;
                color: #555;
            }
        """)

    # Fungsi yang dijalankan saat tombol ditekan
    def on_get_weather(self):
        city_name = self.city_input.text()
        weather = get_weather(city_name)
        
        if weather:
            # Update suhu
            self.temperature_label.setText(f"Suhu: {weather['temperature']}°C")
            
            # Update deskripsi cuaca
            self.description_label.setText(f"Deskripsi: {weather['description'].capitalize()}")
            
            # Update ikon cuaca
            icon_code = weather['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            self.update_weather_icon(icon_url)
        else:
            self.temperature_label.setText("Kota tidak ditemukan")
            self.weather_icon_label.clear()
            self.description_label.setText("Deskripsi: -")

    # Fungsi untuk memperbarui ikon cuaca
    def update_weather_icon(self, icon_url):
        image_data = requests.get(icon_url).content
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)
        self.weather_icon_label.setPixmap(pixmap)
        self.weather_icon_label.setAlignment(Qt.AlignCenter)

# Fungsi utama aplikasi
def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

