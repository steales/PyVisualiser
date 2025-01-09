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