import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import phase5_encrypt, phase5_decrypt

key = {"shift": 5}
text = "Hello World"

print(f"Orignal text: {text}")
encrypted = phase5_encrypt(text, key)
print(f"Encrypted: {encrypted}")
decrypted = phase5_decrypt(encrypted, key)
print(f"decrypted = {decrypted}")

if decrypted == text:
    print("Status: PASSED")

else:
    print("Status: FAILED")
