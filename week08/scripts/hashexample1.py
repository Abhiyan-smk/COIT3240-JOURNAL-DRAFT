# Example of hash function in Python
from cryptography.hazmat.primitives import hashes
h = hashes.Hash(hashes.SHA256())	# Selects hash function
h.update(b"Steven")			# Applies hash function on message
h1 = h.finalize()			# Outputs hash value
print(h1)
h1_hex = h1.hex()			# Convert from bytes to hex
print(h1_hex)

h1_bytes = bytes.fromhex(h1_hex)	# Convert from hex to bytes
print(h1_bytes)
