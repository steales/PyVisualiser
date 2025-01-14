# PyVisualiser
# Author: steales
# Version: 1.2.0
# License: MIT License
# Date: 14th Jan 2025

import sys
import os
import numpy as np
import pyaudio
import wave
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QColor, QIcon, QPixmap
from scipy.ndimage import gaussian_filter1d

class visualiserWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.audio_data = None
        self.setMinimumSize(400, 300)
        self.visualiser_shape = "rectangle"
        self.smoothing_factor = 5

        self.background_image = QPixmap("logo_white.PNG")
        self.image_width = 200
        self.image_height = 200
        self.scaled_image = self.background_image.scaled(
            self.image_width,
            self.image_height,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

    def update_audio_data(self, data):
        smoothed_data = gaussian_filter1d(data, sigma=self.smoothing_factor)
        self.audio_data = smoothed_data
        self.update()

    def toggle_shape(self):
        if self.visualiser_shape == "rectangle":
            self.visualiser_shape = "circle"
        else:
            self.visualiser_shape = "rectangle"
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.scaled_image:
            image_x = (self.width() - self.scaled_image.width()) // 2
            image_y = (self.height() - self.scaled_image.height()) // 2
            painter.drawPixmap(image_x, image_y, self.scaled_image)

        if self.audio_data is None:
            return

        width, height = self.width(), self.height()
        center_x, center_y = width // 2, height // 2
        radius = min(width, height) // 3
        radius *= 0.8

        # Normalize the audio data
        normalised_data = self.audio_data / np.max(np.abs(self.audio_data)) if np.max(np.abs(self.audio_data)) > 0 else self.audio_data

        if self.visualiser_shape == "rectangle":
            # Rectangle visualiser logic
            num_bars = len(self.audio_data)
            bar_width = width / num_bars
            scaling_factor = height / 2

            for i in range(num_bars):
                x = int(i * bar_width)
                current_bar_width = int(bar_width)
                bar_height = int(normalised_data[i] * scaling_factor)
                painter.drawRect(x, center_y - bar_height // 2, current_bar_width, bar_height)

        elif self.visualiser_shape == "circle":
            # Circle visualiser logic with symmetry
            num_points = len(self.audio_data)
            half_points = num_points // 2

            # Draw the top half of the semi-circle
            for i in range(half_points):
                angle = np.pi * i / (half_points - 1)  # Top semi-circle: 0 to π
                x = center_x + int(radius * (1 + normalised_data[i]) * np.cos(angle))
                y = center_y - int(radius * (1 + normalised_data[i]) * np.sin(angle))  # Negative for top semi-circle
                painter.drawLine(center_x, center_y, x, y)

            # Draw the bottom half by mirroring the top
            for i in range(half_points):
                angle = np.pi * i / (half_points - 1)  # Bottom semi-circle: 0 to π
                x = center_x + int(radius * (1 + normalised_data[i]) * np.cos(angle))
                y = center_y + int(radius * (1 + normalised_data[i]) * np.sin(angle))  # Positive for bottom semi-circle
                painter.drawLine(center_x, center_y, x, y)



class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyVisualiser")
        self.setWindowIcon(QIcon("logo_icon.PNG"))

        self.visualiser = visualiserWidget()

        self.play_button = QPushButton("Play")
        self.play_button.setEnabled(False)
        self.play_button.clicked.connect(self.play_audio)

        self.open_button = QPushButton("Open")
        self.open_button.clicked.connect(self.open_file)

        self.toggle_shape_button = QPushButton("Toggle Shape")
        self.toggle_shape_button.clicked.connect(self.visualiser.toggle_shape)

        self.volume_level = QLabel("Volume: 100")
        self.volume_level.setAlignment(Qt.AlignCenter)
        self.volume_level.setFixedHeight(30)

        self.volumeslider = QSlider(Qt.Horizontal)
        self.volumeslider.setRange(0, 100)
        self.volumeslider.setValue(100)
        self.volumeslider.setToolTip("Volume")
        self.volumeslider.valueChanged.connect(self.set_volume)


        control_layout = QHBoxLayout()
        control_layout.addWidget(self.open_button)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.toggle_shape_button)

        volume_layout = QVBoxLayout()
        volume_layout.addWidget(self.volume_level)
        volume_layout.addWidget(self.volumeslider)
        volume_layout.setAlignment(Qt.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.visualiser, stretch = 1)
        main_layout.addLayout(control_layout, stretch = 0)
        main_layout.addLayout(volume_layout, stretch = 0)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_visualiser)
        self.audio_interface = None
        self.audio_stream = None
        self.stream = None
        self.volume = 1

    def set_volume(self, value):
        self.volume = value / 100.0
        self.volume_level.setText(f"Volume: {value}")

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav)")
        if file_path:
            try:
                self.stream = wave.open(file_path, 'rb')
                self.audio_interface = pyaudio.PyAudio()
                self.audio_stream = self.audio_interface.open(
                    format=self.audio_interface.get_format_from_width(self.stream.getsampwidth()),
                    channels=self.stream.getnchannels(),
                    rate=self.stream.getframerate(),
                    output=True
                )
                self.play_button.setEnabled(True)
                file_name = os.path.basename(file_path)
                self.setWindowTitle(f"PyVisualiser - {file_name}")
            except Exception as e:
                print(f"Error opening audio file: {e}")
                self.stream = None

    def play_audio(self):
        if not self.stream:
            return
        
        if self.timer.isActive():
            self.timer.stop()
            self.audio_stream.stop_stream()
            self.play_button.setText("Play")
        else:
            self.timer.start(16)
            self.audio_stream.start_stream()
            self.play_button.setText("Pause")

    def update_visualiser(self):
        if self.stream and self.audio_stream:
            data = self.stream.readframes(1024)
            if len(data) == 0:
                self.timer.stop()
                self.audio_stream.stop_stream()
                self.play_button.setText("Play")
                return
            audio_array = np.frombuffer(data, dtype=np.int16)

            if audio_array.size == 0 or np.max(np.abs(audio_array)) == 0:
                normalised_data = np.zeros_like(audio_array, dtype = float)
            else:
                normalised_data = audio_array / np.max(np.abs(audio_array))
            
            scaled_data = (audio_array * self.volume).astype(np.int16)
            self.visualiser.update_audio_data(normalised_data)
            self.audio_stream.write(scaled_data.tobytes())



    def closeEvent(self, event):
        if self.audio_stream:
            self.audio_stream.stop_stream()
            self.audio_stream.close()
        if self.audio_interface:
            self.audio_interface.terminate()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
