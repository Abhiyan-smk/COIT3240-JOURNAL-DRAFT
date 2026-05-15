# Week 04

## Task 1 – XOR Operation

I tested the XOR operation in Python using two binary values.

- a = 10101010
- b = 11001100

The XOR result was:

- result = 01100110
- decimal = 102

XOR returns `1` when the bits are different and `0` when the bits are the same.

At first the XOR operation looked very basic, but after completing the activity I understood why it is heavily used in cryptography. XOR is reversible, meaning that applying the same XOR operation again using the same key restores the original plaintext.

XOR is commonly used in:
- stream ciphers
- one-time pads
- CBC mode
- CTR mode encryption

While testing the Python script, I noticed that even a small change in the input values completely changed the output value.

![XOR Screenshot](images/week04-task1-xor.png)

---

## Task 2 – Simple Block Cipher (SBC)

I created a simple block cipher in Python. The plaintext was divided into blocks of four characters, and each character was shifted by `+1` to simulate encryption.

Example:
- H became I
- E became F

The plaintext blocks and ciphertext blocks were displayed separately. This demonstrated how block ciphers process fixed-size blocks independently.

Initially I assumed this encryption method was reasonably secure because the ciphertext looked different from the plaintext. However, after testing repeated plaintext blocks, I realised that the same plaintext always produced the same ciphertext output.

This is a weakness because attackers may identify repeating patterns in encrypted data.

![SBC Screenshot](images/week04-task2-sbc.png)

---

### SBC Table Example

Using the SBC lookup table from the tutorial:

- Plaintext = 10110
- Key = 101
- Ciphertext = 01011

Decryption example:
- Ciphertext = 11111
- Key = 011
- Plaintext = 00000

This activity demonstrated how encryption and decryption can be performed using substitution tables and binary operations.

One thing I found interesting was how small binary changes completely altered the ciphertext result.

---

## Task 3 – CBC Mode Encryption

I created a simple CBC (Cipher Block Chaining) style encryption script in Python.

In CBC mode, each plaintext block is XORed with the previous ciphertext block before encryption.

An initialization vector (IV) of `"AAAA"` was used for the first block.

Unlike ECB mode, repeated plaintext blocks do not produce identical ciphertext blocks because each block depends on the previous encrypted block.

While testing the script, I noticed that changing one plaintext block also affected later ciphertext blocks. This helped me understand how chaining works in CBC mode.

Compared with the simple block cipher from the previous task, CBC mode produced ciphertext that appeared much less predictable.

![CBC Screenshot](images/week04-task3-cbc.png)

---

## Task 4 – CTR Mode Encryption

I implemented a simple CTR (Counter) mode style encryption script in Python.

A counter value was used to generate a keystream, and the plaintext was XORed with the keystream to produce ciphertext.

Unlike CBC mode, CTR mode does not depend on previous ciphertext blocks. Each block is encrypted independently using a different counter value.

At first I found CTR mode confusing because it behaves differently from chained block encryption. After testing both encryption and decryption, I understood that CTR mode behaves more similarly to a stream cipher because XOR is applied against a generated keystream.

One important observation was that blocks could be processed independently, which allows parallel encryption and decryption.

![CTR Screenshot](images/week04-task4-ctr.png)

---

## Task 5 – Comparison of ECB, CBC and CTR Modes

I compared simple block encryption, CBC mode and CTR mode.

### ECB / Simple Block Cipher
- Each block is encrypted independently.
- Identical plaintext blocks produce identical ciphertext blocks.
- Patterns in the plaintext may remain visible.
- Weak against pattern analysis.

### CBC Mode
- Each plaintext block is XORed with the previous ciphertext block before encryption.
- Repeated plaintext blocks produce different ciphertext blocks.
- More secure than ECB because patterns are hidden.
- Encryption depends on previous blocks.

### CTR Mode
- Uses a counter to generate a keystream.
- Plaintext is XORed with the keystream.
- Blocks are independent and can be processed in parallel.
- Faster and more flexible than CBC in many situations.

From the experiments, CBC and CTR produced ciphertext that looked far less predictable than the simple block cipher.

Before completing these activities, I did not fully understand why ECB mode is considered insecure. Comparing the outputs directly made the weaknesses much clearer.

---

## Task 6 – AES Encryption in Python

I used the Python `cryptography` library to encrypt and decrypt a message using AES-based Fernet encryption.

The program:
- generated a random encryption key
- encrypted the plaintext message
- decrypted the ciphertext back into the original message

This demonstrated symmetric encryption because the same key was used for both encryption and decryption.

The ciphertext output appeared random and unreadable without the correct key.

One thing I noticed was that the encrypted output changed each time the program was executed, even when the plaintext stayed the same. After reviewing the behaviour, I understood that random initialization data improves security by preventing predictable ciphertext generation.

![AES Screenshot](images/week04-task6-aes.png)

---

## Reflection

This week improved my understanding of how block ciphers operate in different encryption modes and why encryption mode selection is important in practical cryptography.

The XOR exercises showed how simple binary operations form the foundation of many cryptographic systems. Even though XOR is mathematically simple, it becomes very powerful when combined with keys, counters and chaining operations.

The CBC and CTR activities were especially useful because they demonstrated different approaches for protecting confidentiality:
- CBC improves confidentiality by chaining ciphertext blocks together
- CTR generates a keystream using counters and allows independent block processing

Comparing ECB-style encryption with CBC and CTR made the weaknesses of repeated ciphertext patterns much easier to understand.

The AES encryption task using Python demonstrated how modern symmetric encryption works in practical applications. The ciphertext appeared random and unreadable, while successful decryption required the correct key.

Overall, this week improved my understanding of:
- XOR operations
- block ciphers
- ECB weaknesses
- CBC chaining
- CTR keystream encryption
- practical AES encryption

The activities also demonstrated why modern systems avoid ECB mode and instead prefer stronger modes such as CBC, CTR and GCM in real-world security systems.
