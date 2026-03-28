from pycipher import Caesar

plaintext = "HELLO WORLD"
cipher = Caesar(key=3)

encrypted = cipher.encipher(plaintext)
decrypted = cipher.decipher(encrypted)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
