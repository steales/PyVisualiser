# PyVisualiser
# Author: steales
# Version: R1
# License: MIT License
# Date: 9th Jan 2025

import sys
import os
import numpy as np
import pyaudio
import wave
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor

class visualiserWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.audio_data = np.zeros(1024)
        self.setMinimumHeight(200)

    def update_audio_data(self, audio_data):
        self.audio_data = audio_data
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        width = self.width()
        height = self.height()
        center_y = height // 2

        painter.fillRect(0, 0, width, height, QColor("black"))

        num_points = len(self.audio_data)
        x_step = width / num_points

        for i in range(num_points - 1):
            x1 = int(i * x_step)
            x2 = int((i + 1) * x_step)
            y1 = int(center_y - self.audio_data[i] * center_y)
            y2 = int(center_y - self.audio_data[i + 1] * center_y)
            painter.setPen(QColor("green"))
            painter.drawLine(x1, y1, x2, y2)

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyVisualiser")

        self.visualiser = visualiserWidget()

        self.play_button = QPushButton("Play")
        self.play_button.setEnabled(False)
        self.play_button.clicked.connect(self.play_audio)

        self.open_button = QPushButton("Open")
        self.open_button.clicked.connect(self.open_file)

        layout = QVBoxLayout()
        layout.addWidget(self.visualiser)
        layout.addWidget(self.open_button)
        layout.addWidget(self.play_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_visualiser)
        self.audio_interface = None
        self.audio_stream = None
        self.stream = None

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
            
            self.visualiser.update_audio_data(normalised_data)
            self.audio_stream.write(data)

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
