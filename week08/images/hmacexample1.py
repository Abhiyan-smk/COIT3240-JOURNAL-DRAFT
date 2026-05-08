# Example of HMAC
from cryptography.hazmat.primitives import hashes, hmac
key = b"This is my key"			# Secret key
mac = hmac.HMAC(key, hashes.SHA256())	# Select hash algorithm and supply key
mac.update(b"Steven")			# Apply MAC on message
t1 = mac.finalize()			# Output the tag
t1_hex = t1.hex()			# Convert bytes to hex
print(t1_hex)
