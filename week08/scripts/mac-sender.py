'''
Demo of mac.py from sender's perspective
'''

import mac

# Prepare message and key
message = "message to hash"
key_hex = "0123456789012345678901234567890123456789012345678901234567890123"
key = mac.hex_to_binary(key_hex)
print("Original key: " + key_hex)

# Calculate the tag
tag_binary = mac.tag(message, key)
print("Tx message: " + message)

# Convert tag to base64 so can be easily sent across network
tag_text = mac.binary_to_base64(tag_binary)
print("Tx tag: " + tag_text)

# Send the message and tag to other side, e.g., with email or Teams
