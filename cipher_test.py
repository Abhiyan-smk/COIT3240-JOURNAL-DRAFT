from pycipher import Caesar

plaintext = "HELLO WORLD"
cipher = Caesar(key=3)

encrypted = cipher.encipher(plaintext)
decrypted = cipher.decipher(encrypted)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

--- known key decryptiopo E.g---

print("\nKnown Key Decryption:")
print("Ciphertext: pjhigpaxp")
print("Decrypted:", Caesar(15).decipher("pjhigpaxp")


      --- Unknown Key (Brute Force E.g) ---

print("\nBrute Force Attack on 'KHOORZRUOG':")

cipher_text = "KHOORZRUOG"

for i in range(1, 26):
    print(i, Caesar(i).decipher(cipher_text))

--- Unknown Key (Brute Force E.g) ---

print("\nBrute Force Attack on 'KHOORZRUOG':")

cipher_text = "KHOORZRUOG"

for i in range(1, 26):
    print(i, Caesar(i).decipher(cipher_text))
