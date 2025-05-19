"""
Decode sequences of gestures into Morse code and text.
"""
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '--.': 'G', '....': 'H',
    '..': 'I', '--..': 'Z', # Extend this dictionary
}

def decode_morse(morse_sequence):
    return MORSE_CODE_DICT.get(morse_sequence, '?')
