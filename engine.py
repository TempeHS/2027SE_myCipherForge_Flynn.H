"""
CipherForge — Encryption Engine
================================
Author: [Your Name]
Date: 2026

This file contains my custom 5-layer encryption algorithm.

PHASES:
  1. Substitution — Replace characters with different ones
  2. Transposition — Rearrange the order of characters
  3. Key-Dependent — Make output depend on a secret password
  4. Noise Injection — Add fake characters to confuse attackers
  5. Wild Card — My unique invention!

RULES:
  - encrypt() MUST be reversible
  - decrypt(encrypt(message)) MUST return the original message
"""


def simple_shift(text, shift):
    """
    Shift every character by 'shift' positions.

    This is a simple Caesar cipher that works on ALL printable characters,
    not just letters. It wraps around using modular arithmetic.

    Args:
        text: The string to encrypt
        shift: How many positions to shift (positive = forward)

    Returns:
        The encrypted string
    """
    result = ""

    for char in text:
        if 32 <= ord(char) <= 126:
            position = ord(char) - 32

            new_position = (position + shift) % 95

            result += chr(new_position + 32)

        else:
            # Keep non-printable characters unchanged
            result += char

    return result


def simple_unshift(text, shift):
    """
    Reverse the simple_shift encryption.

    Decryption is just shifting in the opposite direction!

    Args:
        text: The encrypted string
        shift: The same shift value used for encryption

    Returns:
        The decrypted (original) string
    """
    # Decryption = shifting backwards (negative)
    return simple_shift(text, -shift)
