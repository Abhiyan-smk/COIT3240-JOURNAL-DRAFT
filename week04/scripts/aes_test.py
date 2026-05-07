from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Hello Applied Cryptography"

encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print("Key:")
print(key)

print("\nEncrypted:")
print(encrypted)

print("\nDecrypted:")
print(decrypted.decode())
