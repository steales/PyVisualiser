### WARNING to all users who currently suffer from a migraine, epilepsy or other photosensitive conditions - this program produces fast flashing effects!

<center> <img src="https://i.ibb.co/mDCmYTt/IMG-0656.png" alt="PyVisualiser Logo" border="0"> </center>

# PyVisualiser
A simple python real-time audio visualiser build using PyQt5, NumPy, SciPy and PyAudio

## Features
- Play '.wav' audio files
- Realtime waveform visualisation
- Simple GUI built using PyQt5
- Playback options (play, pause)
- Dynamic window title that displays the currently loaded file
- Button to allow the waveform to be rendered in different ways
- Live volume adjustment

## Requirements
To run this project, please make sure you have the following installed:
- Python 3.8 or higher
- PyQt5
- PyAudio
- NumPy
- SciPy

You can install the required libraries using pip:
```bash
pip install pyqt5 pyaudio numpy scipy
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
- No current way to view timer / seek
- Volume slider only changes the volume of the window, instead of changing the volume of the audio data - so no visible change to the waveform occurs

## License
This project is licensed under the MIT License. Please check the `LICENSE` file for more information.

## Images
<img src="https://i.ibb.co/HCc4tSs/image.png" alt="image" border="0" width="300"> <img src="https://i.ibb.co/ZLC76sW/main.png" alt="main" border="0" width="300"> <img src="https://i.ibb.co/VDG9qQ0/image.png" alt="image" border="0" width="300"> <img src="https://i.ibb.co/2ZRLc3r/image.png" alt="image" border="0" width="300"> <img src="https://i.ibb.co/8DQp9cR/image.png" alt="image" border="0" width="300"> <img src="https://i.ibb.co/12Nnm9X/image.png" alt="image" border="0" width="300">

### Additional Credits
Thank you to Leebawk for creating the logo :]
