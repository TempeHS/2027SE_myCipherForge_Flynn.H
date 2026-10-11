"""Test the full Phase 1 + 2 + 3 + 4 pipeline.

Run from the project root with:  python tests/test_phases_1_2_3_4.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import encrypt, decrypt

key = {
    "shift": 5,
    "block_size": 4,
    "password": "CIPHER",
    "noise_interval": 3,
    "noise_char": "~",
}

messages = [
    "Hello World!",
    "CipherForge",
    "Encryption",
    "The eagle flies at midnight",
    "Testing all 5 phases",
    "Tempe High School",
]


for message in messages:
    print(f"\nOriginal:  {message}")

    encrypted = encrypt(message, key)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")

    print(f"Match: {message == decrypted}")
