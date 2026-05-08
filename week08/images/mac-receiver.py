'''
Demo of mac.py from receiver's perspective
'''
import mac

# Secret MAC key must be known by receiver
key_hex = "0123456789012345678901234567890123456789012345678901234567890123"

# message and tag received
rx_message = "message to hash"
rx_tag_text = "F4VAdKHlf/5MBIhJz+C9py1yoCoBhspsRA0SSX4FibE="

# Convert base64 tag back to binary
rx_tag_binary = mac.base64_to_binary(rx_tag_text)

# Verify
key = mac.hex_to_binary(key_hex)
print("Rx message: " + rx_message)
print("Rx tag: " + rx_tag_text)
print("Key: " + key_hex)
r = mac.verify(rx_message, key, rx_tag_binary)
print("Verified? " + str(r))