from engine import phase1_decrypt

ciphertext = "^lsjvtl'{v'JpwolyMvynl("

for shift in range(95):
    key = {"shift": shift}
    attempt = phase1_decrypt(ciphertext, key)
    if "Welcome" in attempt or "welcome" in attempt:
        print(f"CRACKED! Shift {shift}: {attempt}")
        break
