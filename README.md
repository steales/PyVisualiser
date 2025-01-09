# PyVisualiser
A simple python real-time audio visualiser build using PyQt5, NumPy and PyAudio

## Features
- Play '.wav' audio files
- Realtime waveform visualisation
- Simple GUI built using PyQt5
- Playback options (play, pause)
- Dynamic window title that displays the currently loaded file

## Requirements
To run this project, please make sure you have the following installed:
- Python 3.8 or higher
- PyQt5
- PyAudio
- NumPy

You can install the required libraries using pip:
```bash
pip install pyqt5 pyaudio numpy
```

## How to Use

1. Clone this repository
```bash
git clone https://github.com/steales/PyVisualiser.git
cd PyVisualiser
```
2. Run the Python script
```bash
python main.py
```
3. Use the "Open" button to open a `.wav` file
4. Press "Play" to begin playback

## Known Issues
- Currently only supports `.wav` files. `.mp3` support can be added using additional libraries such as `pydub`
- No current way to change playback volume
- No current way to view timer / seek

## License
This project is licensed under the MIT License. Please check the `LICENSE` file for more information.

## Images
![alt text](https://ibb.co/6n5LRhg)
![alt text](https://private-user-images.githubusercontent.com/84470105/401573578-a0572288-7d15-42c5-a70d-d78fc7cda93e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzY0MzI2NzAsIm5iZiI6MTczNjQzMjM3MCwicGF0aCI6Ii84NDQ3MDEwNS80MDE1NzM1NzgtYTA1NzIyODgtN2QxNS00MmM1LWE3MGQtZDc4ZmM3Y2RhOTNlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAxMDklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMTA5VDE0MTkzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRiN2FmNDZiNDc4OGU1ZGNjMTBjZDgzZjIwMmFlOTA2ZGFkZGQ2MWEwODBjNTA5Y2Q3MTM3N2M5MjdlMDk0NWEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.3qwW2LIT6gLGZC2PAgHg4Bj7XWUu6TmaojDziG-y68w)
