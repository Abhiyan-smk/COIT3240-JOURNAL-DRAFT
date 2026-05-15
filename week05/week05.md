# Week 05

## Task 1 – RSA Key Generation

RSA is an asymmetric encryption algorithm that uses two separate keys:
- public key
- private key

The public key can be shared publicly, while the private key must remain secret.

I manually generated an RSA key pair using small prime numbers.

Chosen primes:
- p = 181
- q = 191

Calculated values:
- n = p × q = 34571
- Φ(n) = (181 − 1)(191 − 1) = 34200

Chosen public exponent:
- e = 7

Calculated private exponent:
- d = 19543

Public key:
- PU = (e = 7, n = 34571)

Private key:
- PR = (d = 19543, n = 34571)

Values that must remain secret:
- d
- p
- q

Values that may be public:
- e
- n

At first the calculations looked complicated because several mathematical steps were involved. After working through the equations manually, I understood how the relationship between `e`, `d` and `Φ(n)` allows RSA encryption and decryption to function correctly.

One thing I found interesting was that RSA security depends heavily on the difficulty of factoring large prime numbers.

![RSA Generation Screenshot](images/week05-task1-rsa-generation.png)

---

## Task 2 – RSA Encryption and Decryption

I tested RSA encryption and decryption using the RSA key pair generated previously.

Chosen plaintext:
- M = 123

Encryption formula:

C = M^e mod n

Calculated ciphertext:
- C = 6238

Decryption formula:

M = C^d mod n

After decrypting the ciphertext using the private key, the original plaintext value `123` was successfully recovered.

This demonstrated how RSA uses:
- the public key for encryption
- the private key for decryption

Initially I assumed RSA encryption worked similarly to symmetric encryption from the previous week. After completing the calculations, I understood that RSA uses mathematically related keys instead of sharing the same secret key.

![RSA Encryption Screenshot](images/week05-task2-rsa-encryption.png)

---

## Task 3 – RSA Keys in OpenSSL

I generated a real RSA key pair using OpenSSL. I created a 2048-bit RSA private key and then extracted the matching public key.

Commands used:

```bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out private_key.pem
```

```bash
openssl pkey -in private_key.pem -pubout -out public_key.pem
```

```bash
ls -l *.pem
```

The generated files included:
- `private_key.pem`
- `public_key.pem`

I noticed that the private key file was significantly larger and had stricter permissions than the public key file.

This activity demonstrated how RSA keys are generated in real systems instead of using small manual examples.

![RSA OpenSSL Key Generation Screenshot](images/week05-task3-rsa-key-generation.png)

---

## Task 4 – RSA Encryption in OpenSSL

I used OpenSSL to encrypt and decrypt a confidential text message using RSA public and private keys.

First, I created a plaintext message file:

```bash
echo "This is my Week 5 RSA secret message." > message.txt
```

The message was encrypted using the RSA public key:

```bash
openssl pkeyutl -encrypt -pubin -inkey public_key.pem -in message.txt -out message.enc
```

This generated an encrypted ciphertext file named `message.enc`.

The ciphertext could not be read directly because the plaintext had been transformed into encrypted binary data.

Next, I decrypted the ciphertext using the RSA private key:

```bash
openssl pkeyutl -decrypt -inkey private_key.pem -in message.enc -out message_decrypted.txt
```

After decryption, the original plaintext message was successfully recovered inside `message_decrypted.txt`.

This activity demonstrated how RSA public key cryptography provides confidentiality because only the matching private key can decrypt the encrypted message.

![RSA OpenSSL Encryption Screenshot](images/week05-task4-rsa-openssl-encryption.png)

---

## Task 5 – Digital Signatures in OpenSSL

I created and verified a digital signature using OpenSSL and RSA keys.

First, I generated a SHA-256 digital signature for the plaintext message using the RSA private key:

```bash
openssl dgst -sha256 -sign private_key.pem -out message.sig message.txt
```

This produced a signature file called `message.sig`.

Next, I verified the signature using the RSA public key:

```bash
openssl dgst -sha256 -verify public_key.pem -signature message.sig message.txt
```

The verification result displayed:

```bash
Verified OK
```

This confirmed that:
- the message had not been modified
- the signature was created using the correct private key

Initially I thought encryption and digital signatures were performing the same security function. After completing the activity, I understood that they provide different protections:
- encryption protects confidentiality
- digital signatures verify authenticity and integrity

I also noticed that even a small modification to the original message would cause signature verification to fail.

![Digital Signature Screenshot](images/week05-task5-digital-signature.png)

---

## Reflection

This week introduced public key cryptography and RSA encryption. Unlike symmetric encryption algorithms such as AES, RSA uses two mathematically related keys instead of a shared secret key.

The manual RSA calculations helped me understand how the mathematical relationships between `p`, `q`, `n`, `e` and `d` are used to generate RSA key pairs.

At first the modular arithmetic calculations were slightly confusing, especially the relationship between the public exponent and private exponent. Working through the calculations step-by-step made the encryption and decryption process much clearer.

Using OpenSSL provided practical experience with real RSA implementations. I learned how to:
- generate RSA key pairs
- extract public keys
- encrypt and decrypt messages
- create and verify digital signatures

One important insight from this week was understanding the difference between confidentiality and authenticity:
- encryption protects confidential information from unauthorized access
- digital signatures verify the sender and confirm that data has not been modified

The OpenSSL activities also demonstrated how RSA is used in practical systems such as:
- HTTPS
- SSH
- digital certificates
- secure communications

Overall, this week improved my understanding of:
- public key cryptography
- RSA mathematics
- key generation
- RSA encryption and decryption
- digital signatures
- authentication and integrity
