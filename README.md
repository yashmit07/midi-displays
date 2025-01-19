# MIDI Visualization

A web-based MIDI visualization that displays colored circles in response to MIDI input. The screen is divided into three sections, each responding to different note ranges with different colors.

## Setup

1. Make sure you have Python installed
2. Clone this repository
3. Run the server:
   ```bash
   python server.py
   ```
4. The webpage should open automatically in your default browser
5. Allow MIDI access when prompted
6. Play your MIDI device to see the visualization

## Note Ranges

- Notes 72-83 (C4-B4): Red circles (left section)
- Notes 84-95 (C5-B5): Green circles (middle section)
- Notes 96+ (C6 and above): Blue circles (right section)

## Requirements

- A modern web browser that supports WebMIDI (Chrome or Edge recommended)
- A connected MIDI device
- Python 3.x