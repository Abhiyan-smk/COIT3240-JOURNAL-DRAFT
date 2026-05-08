# Example of HMAC
from cryptography.hazmat.primitives import hashes, hmac
import os
from cryptography import exceptions

# Sender calculating the tag for a message
key = os.urandom(32)			# Generate a random key
print(key.hex())
mac = hmac.HMAC(key, hashes.SHA256())	# Select hash algorithm and supply key
mac.update(b"Steven")			# Apply MAC on message
t1 = mac.finalize()			# Output the tag
t1_hex = t1.hex()			# Convert bytes to hex
print(t1_hex)

# Receiver verifies a tag for a message
rx_message = b"Steven1"
rx_key = key
rx_tag = t1
mac = hmac.HMAC(rx_key, hashes.SHA256())
mac.update(rx_message)
try:
	mac.verify(rx_tag)
	result = "Message verified. Well done!"
except exceptions.InvalidSignature:
	result = "Oh no! Something is wrong"

print(result)
