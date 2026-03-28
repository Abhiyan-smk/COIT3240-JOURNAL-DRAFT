from pycipher import caesar

plaintext = "HELLO WORLD"
cipher = caesar(key=3)
encrypted = cipher.encipher(plaintext)
decrypt =cipher.decipher(encrypted)
print("plintext:" , plaintext)
Print("Encrypted:" ,encrypted)
print("decrypted:" , decrypted)
