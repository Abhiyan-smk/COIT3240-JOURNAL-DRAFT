# Week 08

## Task 1 – Hash Functions

A cryptographic hash function converts input data into a fixed-length output called a hash or digest.

Hash functions are designed to:
- produce a unique output for different inputs
- be one-way functions
- detect changes to data

I tested a SHA256 hash function in Python using the `cryptography` library.

The program generated a SHA256 hash value for the plaintext message:
- "Steven"

The output displayed:
- the raw byte hash value
- the hexadecimal hash value

Even a small change to the plaintext produces a completely different hash output.

![Hash Example](images/week08-task1-hash-example.png)

---

## Task 2 – Modified Hash Function

I modified the original hash example by:
- changing SHA256 to SHA512
- changing the plaintext message

The modified program generated a longer hash value because SHA512 produces a 512-bit digest instead of a 256-bit digest.

This activity demonstrated that:
- different hash algorithms produce different digest lengths
- changing the input message completely changes the hash output

This behaviour is called the avalanche effect.

![Modified Hash Example](images/week08-task2-modified-hash.png)

---

## Task 3 – HMAC Example

HMAC stands for Hash-based Message Authentication Code.

Unlike normal hashing, HMAC uses:
- a cryptographic hash function
- a shared secret key

This allows both integrity and authentication to be verified.

I tested HMAC generation using Python and SHA256.

The program:
- used a secret key
- generated an authentication tag for a message

The generated HMAC value can later be verified by another user who also knows the shared secret key.

![HMAC Example 1](images/week08-task3-hmac-example1.png)

---

## Task 4 – HMAC Verification

I tested HMAC verification using Python.

The program:
- generated an HMAC tag
- verified the received message and tag
- tested what happens when the message changes

When the original message was verified, the authentication process succeeded.

After modifying the message, the verification process failed and displayed:

- "Oh no! Something is wrong"

This demonstrated that HMAC can detect message modification and protect data integrity.

![HMAC Verification](images/week08-task4-hmac-example2.png)

---

## Task 5 – MAC Sender

I tested a Message Authentication Code (MAC) sender program.

The sender program:
- created a plaintext message
- generated a MAC tag using a shared secret key

The output displayed:
- the original secret key
- transmitted message
- generated MAC tag

The MAC tag can later be verified by the receiver.

![MAC Sender](images/week08-task5-mac-sender.png)

---

## Task 6 – MAC Receiver Verification

I tested the MAC receiver program.

The receiver:
- received the message
- received the MAC tag
- verified the integrity of the message

The verification result displayed:

- Verified? True

This confirmed that:
- the message was authentic
- the message contents were unchanged

![MAC Receiver Verification](images/week08-task6-mac-receiver.png)

---

## Task 7 – Modified Message Detection

I modified the received message while keeping the original MAC tag unchanged.

After verification, the output displayed:

- Verified? False

This demonstrated that:
- changing the message invalidates the MAC
- MAC verification can detect tampering
- integrity protection prevents unauthorized message modification

![Modified Message Verification Failure](images/week08-task7-mac-modified-message.png)

---

## Reflection

This week introduced cryptographic hash functions, HMACs and message authentication codes.

The practical Python activities demonstrated how hashing can verify data integrity and how HMAC adds authentication using a shared secret key.

One important observation was that hash functions are deterministic:
- the same input always produces the same output
- even a very small change completely changes the hash value

The HMAC and MAC activities demonstrated how integrity and authentication are implemented in real communication systems.

The modified message verification task was particularly important because it demonstrated that attackers cannot change messages without detection when MAC protection is used correctly.

This week also helped me understand how:
- hashes verify integrity
- HMAC verifies integrity and authentication
- MACs detect message tampering

These concepts are widely used in:
- TLS
- HTTPS
- APIs
- secure communications
- digital authentication systems

Overall, the practical exercises improved my understanding of integrity protection, authentication and secure message verification.
