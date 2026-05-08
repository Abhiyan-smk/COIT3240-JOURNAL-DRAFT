'''
MAC demo using Python cryptography library
'''

import logging
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend
from cryptography import exceptions
import base64

logger = logging.getLogger("MAC")


def tag(message, key):
    '''
    Create a MAC tag for message given the secret key
    '''

    # Load backend
    backend = default_backend()

    # Convert the message string to bytes
    message_bytes = message.encode('utf-8')

    # Calculate tag from key, hash algorithm and message
    # This demo is using HMAC
    h = hmac.HMAC(key, hashes.SHA256(), backend=backend)
    h.update(message_bytes)
    tag = h.finalize()

    return tag


def verify(message, key, tag):
    '''
    Verify the received message and tag are correct
    '''

    # Load backend
    backend = default_backend()

    # Convert the message string to bytes
    message_bytes = message.encode('utf-8')

    # Calculate tag from key, hash algorithm and message
    # This demo is using HMAC
    h = hmac.HMAC(key, hashes.SHA256(), backend=backend)
    h.update(message_bytes)
    try:
        h.verify(tag)
        result = True
    except exceptions.InvalidSignature:
        result = False

    return result


def binary_to_base64(b):
    '''
    Convert binary into Base64 
    '''

    return base64.b64encode(b).decode('utf-8')


def base64_to_binary(b64):
    '''
    Convery base64 to binary
    '''

    return base64.b64decode(b64)


def binary_to_hex(b):
    '''
    Convert binary to hex
    '''

    return b.hex()


def hex_to_binary(h):
    '''
    Convert hex to binary
    '''

    return bytes.fromhex(h)


if __name__ == '__main__':
    # A test message and key
    message = "message to hash"
    key_hex = "0123456789012345678901234567890123456789012345678901234567890123"
    key = hex_to_binary(key_hex)
    print("Original key: " + key_hex)

    # Calculate the tag
    tag_binary = tag(message, key)
    print("Tx message: " + message)

    # Convert tag to base64 so can be easily sent across network
    tag_text = binary_to_base64(tag_binary)
    print("Tx tag: " + tag_text)

    # Send the message and tag to other side
    rx_tag_text = tag_text
    rx_message = message

    # Convert base64 tag back to binary
    print("Transmissing message and tag ...")
    rx_tag_binary = base64_to_binary(rx_tag_text)

    # Verify
    print("Rx message: " + rx_message)
    print("Rx tag: " + rx_tag_text)
    print("Key: " + key_hex)
    r = verify(rx_message, key, rx_tag_binary)
    print("Verified? " + str(r))

    # Verify with the wrong message
    rx_message = "This is wrong"
    print("Rx message: " + rx_message)
    print("Rx tag: " + rx_tag_text)
    print("Key: " + key_hex)
    r = verify(rx_message, key, rx_tag_binary)
    print("Verified? " + str(r))

    # Verify with the wrong key
    rx_message = message
    wrongkey_hex = "1123456789012345678901234567890123456789012345678901234567890123"
    wrongkey = hex_to_binary(wrongkey_hex)

    print("Rx message: " + rx_message)
    print("Rx tag: " + rx_tag_text)
    print("Key: " + wrongkey_hex)
    r = verify(rx_message, wrongkey, rx_tag_binary)
    print("Verified? " + str(r))
