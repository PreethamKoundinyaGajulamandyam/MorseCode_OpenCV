import os

# Ask user where to create the project
user_path = input("Enter the full path where you want to create the project (e.g., /Users/preetham/Desktop): ").strip()
base_dir = os.path.join(user_path, "MorseCode_OpenCV")

folders = [
    "src",
    "assets",
    "data",
    "notebooks",
    "tests"
]

files_with_content = {
    "src/main.py": '''"""
Main script for MorseCode_OpenCV
"""
from src.gesture_detection import detect_gesture
from src.morse_decoder import decode_morse
from src.utils import draw_text

def main():
    print("Starting Morse Code Detection via Hand Gestures...")
    # Initialize camera and detection loop here

if __name__ == "__main__":
    main()
''',

    "src/gesture_detection.py": '''"""
Handles hand detection and gesture classification.
"""
import cv2
import mediapipe as mp

def detect_gesture(frame):
    # Stub for gesture detection logic using MediaPipe
    return None
''',

    "src/morse_decoder.py": '''"""
Decode sequences of gestures into Morse code and text.
"""
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '--.': 'G', '....': 'H',
    '..': 'I', '--..': 'Z', # Extend this dictionary
}

def decode_morse(morse_sequence):
    return MORSE_CODE_DICT.get(morse_sequence, '?')
''',

    "src/utils.py": '''"""
Utility functions: drawing, timers, buffering, etc.
"""
def draw_text(frame, text, position=(50, 50)):
    # Add OpenCV putText logic
    pass
''',

    "src/config.py": '''"""
Global configuration parameters.
"""
DOT_THRESHOLD = 0.5  # seconds
PAUSE_THRESHOLD = 1.0  # seconds
''',

    "README.md": "# MorseCode_OpenCV\n\nDetect Morse code using hand gestures and OpenCV.\n",
    "requirements.txt": "opencv-python\nmediapipe\nnumpy\n",
    ".gitignore": "__pycache__/\n*.pyc\n",
    "LICENSE": "MIT License\n"
}

# Create folders
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# Create files
for file_path, content in files_with_content.items():
    full_path = os.path.join(base_dir, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)

print(f"✅ MorseCode_OpenCV project created at: {base_dir}")
