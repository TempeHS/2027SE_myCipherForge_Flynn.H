"""Test the master encrypt/decrypt with Phase 1 wired in.

Run from the project root with:  python tests/test_master_phase1.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import encrypt, decrypt

key = {"shift": 7}
message = "My secret message 123!"

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print(f"Success: {decrypted == message}")
