<img width="522" height="666" alt="image" src="https://github.com/user-attachments/assets/3fb3ab65-89dd-41c1-8143-77049c82ac06" />## Week 02 journal Entry
## COIT3240 Applied Cryptography -classical Cipher

## Overview
In this week i really statrted working on  classical ciphers in hands on way  rather than just  reading about them. The tutorials tasks helped me to think  carefully about  how  the ciphers actually worked. In the tutorial we need to do it manually first before using python later on and this kind of things make me  feel a lot of more practical than week 1 which  was mostly setup and getting  my environment ready for comingup weeks.
A Python virtual environment was created to manage dependencies. The `pycipher` library was installed and used to implement classical cipher operations. This ensured that all cryptographic testing was done in an isolated and controlled environment.
## Task Completed
## Task 1: Week 2 Quiz
i have completed the quizes before doing  the tutorials works which helped me refresh the main concepts from the lecture and the classical ciphers notes. I also found the questions on substitution VS transposition cipher straightforward after watching the lecture.I initially answered one question wrong  like i got confused  the vignere cipher (polyalphabetic substitution) with the playfair cipher (diagraph substitution) and theni have corrected myself by re-reading the lecture slides before the tutorial started. The lecture materials  was very clear for understanding classicla ciphers and uses of its logics for encryptions not because they are strong in real security setting. What stood out for me is that  the unit kept linking to old cipher tomoedern ideas subsitution, permutations and brute force attacks.

## Task 2: Caesar Decrypt (Key 15) — Manual
Ciphertext:phjigpaxp
The caesar cipher shift each letters by a fixed key , in order todecrypt ,i have shited  each letters back by 15 position (or forward by  26-15= 11 position).
Alphabet position (0-indexed):a=0, b=1,c=2,d=3,.....z=25
![IMG_2496](https://github.com/user-attachments/assets/af764933-0a6a-4842-ab77-0caacc87ae63)
## Task 3: Caesar Cipher using Python (Pycipher)  
The `pycipher` library was used to verify encryption and decryption results. This allowed the cipher to be tested programmatically rather than manually.
<img width="898" height="253" alt="image" src="https://github.com/user-attachments/assets/a0652e17-0b77-4e24-981f-89d09a90a818" />
 - the image shows the plaintext: AUSTRALIA  and it's Ciphertext: PHJIGPAXP and plaintext: BELGIUM and ciphertext: KNUPRDV
 
A Caesar cipher was implemented using Python which is also shown in the below image which represents that the plain text was correctly encrypted to "KHOORZRUOG" and successfully decrypted back to "HELLOWORLD". This confirms that the implementation is functioning correctly.

<img width="940" height="300" alt="image" src="https://github.com/user-attachments/assets/ef63863b-9fa6-417d-a2c3-9b9918233df6" />

This confirmed that both encryption and decryption were working correctly. One important observation was that spaces were removed during processing, which highlights how implementation details can affect output.

## Task 4: Caesar Decrypt without Key —Brute Force Manual and Pycipher
Since the key is unknown, I have used a brute force approach: try all 26 possible keys and looking for a meaningful English word.
<img width="522" height="666" alt="image" src="https://github.com/user-attachments/assets/820ecdd9-9986-473d-ae5c-ebf3cadc94a6" />
- Screenshot showing BELGIUM output
  This task demoonstrated that even wthout knowing the key , classical ciphers can be broken by analysing outputs and identifying meaningful patterns in language.

## Task 5: Implement Caesar Cipher in Python
The Caesar cipher was implemented using 'Pycipher' library in python. Thisapproach has all0wed to encrypt and ecrypt the process to be tetsted efficiently without manually coding the alogrithms from the scratch. The following script was used 

## Brute Force Attack

A brute force approach was implemented using Python to test all possible Caesar cipher keys (1–25). The output displayed all possible decrypted results, making it easy to identify the correct plaintext:

HELLOWORLD (key = 3)

This clearly demonstrated that the Caesar cipher is highly insecure due to its very small key space. An attacker can easily recover the original message by checking all possibilities.

## Security Analysis

Although the Caesar cipher functions correctly, it provides almost no real security. The main weaknesses include:

- extremely small key space
- predictable substitution pattern
- vulnerability to brute force attacks
- reliance on recognisable language

This shows that correctness of encryption does not guarantee security.

## Challenges Encountered

Several issues were encountered during this week:

- syntax errors in Python (missing colons, incorrect indentation)
- incorrect module name usage (`picipher` instead of `pycipher`)
- confusion between terminal commands and Python interpreter
- minor Git tracking issues with untracked files

These were resolved by carefully reviewing commands and understanding the correct workflow.

## Reflection

This week significantly improved my understanding of how encryption works in practice. Writing and testing the Caesar cipher made the process much clearer than just reading theory. The most important insight was that a cipher can be logically correct but still insecure.

The brute force exercise was particularly useful, as it showed how quickly a weak cipher can be broken. This provides a strong foundation for understanding why modern cryptographic systems require much larger key spaces and more complex algorithms.

## Evidence of Work Completed

The following evidence supports the work completed this week:

- Python virtual environment setup
- installation of `pycipher`
- Caesar cipher implementation script (`cipher_test.py`)
- successful encryption and decryption output
- brute force attack output showing all key possibilities
- decryption of ciphertexts (AUSTRALIA and BELGIUM)
- Git commits and successful push to repository

## References

- pycipher documentation: https://pycipher.readthedocs.io/
- Week 2 lecture slides and tutorial materials


