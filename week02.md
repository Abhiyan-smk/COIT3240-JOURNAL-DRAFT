## Overview
 In this week i really statrted working on  classical ciphers in hands on way  rather than just  reading about them. The tutorials tasks helped me to think  carefully about  how  the ciphers actually worked. In the tutorial we need to do it manually first before using python later on and this kind of things make me  feel a lot of more practical than week 1 which  was mostly setup and getting  my environment ready for coming weeks.
##Quiz and Lectures
i have completed the quizes before doing  the tutorial;s works  which helped me refresh the main concepts from the lecture and the classical ciphers notes. The lecture materials  was very clear for understanding classicla ciphers and uses of its logics for encryptions not because they are strong in real security setting. What stood out for me is that  the unit kept linking to old cipher tomoedern ideas subsitution, permutations nad brute force attacks.
## Environment Setup
A Python virtual environment was created to manage dependencies. The `pycipher` library was installed and used to implement classical cipher operations. This ensured that all cryptographic testing was done in an isolated and controlled environment.

## Caesar Cipher Implementation

A Caesar cipher was implemented using Python. The plaintext:

HELLO WORLD

was encrypted using a key of 3, producing:

KHOORZRUOG

The decrypted result returned:

HELLOWORLD

This confirmed that both encryption and decryption were working correctly. One important observation was that spaces were removed during processing, which highlights how implementation details can affect output.

## Known-Key Decryption

A ciphertext was decrypted using a known key:

pjhigpaxp (key = 15)

The output obtained was:

AUSTRALIA

This demonstrated how the Caesar cipher works when the key is known and reinforced understanding of shifting characters within the alphabet.

## Decryption Without Known Key

A second ciphertext was analysed without knowing the key:

knuprdv

Different key values were tested until meaningful plaintext appeared. The correct result was:

BELGIUM (key = 9)

This task showed that classical ciphers can often be broken by testing possibilities and recognising valid language patterns, rather than relying purely on mathematical methods.

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


