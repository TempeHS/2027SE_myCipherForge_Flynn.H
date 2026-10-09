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


def phase1_encrypt(text, key):
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
    shift = key.get("shift", 5)
    for char in text:
        if 32 <= ord(char) <= 126:
            position = ord(char) - 32

            new_position = (position + shift) % 95

            result += chr(new_position + 32)

        else:
            # Keep non-printable characters unchanged
            result += char

    return result


def phase1_decrypt(text, key):
    """
    Phase 1: Reverse the substitution.

    Decryption shifts in the OPPOSITE direction (subtracts instead of adds).

    Args:
        text: The encrypted string
        key: Dictionary containing the same encryption settings

    Returns:
        The decrypted (original) string
    """

    shift = key.get("shift", 5)

    result = ""

    for char in text:
        if 32 <= ord(char) <= 126:
            position = ord(char) - 32
            new_position = (position - shift) % 95
            result += chr(new_position + 32)

        else:
            result += char

    return result


def phase2_encrypt(text, key):
    """
    Phase 2: Transposition — Rearrange character positions.

    Uses block reversal: split into blocks and reverse each one.
    This layer changes WHERE each character is (its position).

    Args:
        text: The string to transform (already Phase 1 encrypted)
        key: Dictionary containing encryption settings

    Returns:
        The transposed string with characters rearranged
    """

    # Get block size from key (default to 4 if not specified)
    block_size = key.get("block_size", 4)

    result = ""

    for i in range(0, len(text), block_size):
        block = text[i : i + block_size]
        result += block[::-1]

    return result


def phase2_decrypt(text, key):
    """
    Phase 2: Reverse the transposition.

    For block reversal, decryption is the same as encryption!
    Reversing a reversed block returns the original.

    Args:
        text: The transposed string
        key: Dictionary containing the same encryption settings

    Returns:
        The un-transposed string
    """

    block_size = key.get("block_size", 4)
    result = ""

    for i in range(0, len(text), block_size):
        block = text[i : i + block_size]
        result += block[::-1]

    return result


def phase3_encrypt(text, key):
    """
    Phase 3: Password-Dependent — Variable shifts based on password.

    Each character is shifted by a different amount determined by
    the corresponding character in the repeating password.
    This destroys frequency patterns!

    Args:
        text: The string to transform (already Phase 1+2 encrypted)
        key: Dictionary containing encryption settings

    Returns:
        The password-encrypted string
    """
    # Get password from key (default to "SECRET" if not specified)

    password = key.get("password", "SECRET")

    result = ""

    for i, char in enumerate(text):
        if 32 <= ord(char) <= 126:
            password_char = password[i % len(password)]
            password_shift = ord(password_char) % 95

            position = ord(char) - 32
            new_position = (position + password_shift) % 95
            result += chr(new_position + 32)
        else:
            result += char
    return result


def phase3_decrypt(text, key):
    """
    Phase 3: Reverse the password-dependent encryption.

    CRITICAL: Must use the SAME password that was used for encryption!
    Wrong password = garbage output.

    Args:
        text: The encrypted string
        key: Dictionary with the SAME password used for encryption

    Returns:
        The decrypted string (if password is correct)
    """
    password = key.get("password", "SECRET")

    result = ""

    for i, char in enumerate(text):
        if 32 <= ord(char) <= 126:
            # Get same password character for this position
            password_char = password[i % len(password)]
            password_shift = ord(password_char) % 95

            # SUBTRACT the shift to reverse encryption
            position = ord(char) - 32
            new_position = (position - password_shift) % 95
            result += chr(new_position + 32)
        else:
            result += char

    return result


def encrypt(text, key):
    """
    CipherForge Master Encryption — Applies all 5 phases.

    Currently implemented: Phase 1 only
    Coming soon: Phases 2-5

    Args:
        text: The plaintext to encrypt
        key: Dictionary with settings for all phases

    Returns:
        Fully encrypted string
    """
    # Phase 1: Substitution
    result = phase1_encrypt(text, key)

    # Phase 2: Transposition — change WHERE characters are
    result = phase2_encrypt(result, key)

    # Phase 3: Password-Dependent — destroy frequency patterns
    result = phase3_encrypt(result, key)

    # TODO: Phase 4 — Noise Injection
    # result = phase4_encrypt(result, key)

    # TODO: Phase 5 — Wild Card
    # result = phase5_encrypt(result, key)

    return result


def decrypt(text, key):
    """
    CipherForge Master Decryption — Reverses all 5 phases.

    IMPORTANT: Phases must be reversed in OPPOSITE order!
    Encrypt: 1 → 2 → 3 → 4 → 5
    Decrypt: 5 → 4 → 3 → 2 → 1

    Args:
        text: The encrypted text
        key: Same key used for encryption

    Returns:
        Original plaintext
    """
    result = text

    # TODO: Phase 5 — Reverse Wild Card (first!)
    # result = phase5_decrypt(result, key)

    # TODO: Phase 4 — Reverse Noise Injection
    # result = phase4_decrypt(result, key)

    # Phase 3: Reverse Password-Dependent
    result = phase3_decrypt(result, key)

    # Phase 2: Reverse Transposition
    result = phase2_decrypt(result, key)

    # Phase 1: Reverse Substitution (last!)
    result = phase1_decrypt(result, key)

    return result
