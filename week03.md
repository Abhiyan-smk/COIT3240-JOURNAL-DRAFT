## Week 03 Journal Entry 
## COIT3240 Applied Cryptography
## Introduction

This week I have focused on understanding encryption techniques and attack concepts through practical implementation. The main objective was to explore how block ciphers such as DES operate, how different modes of operation affect security, and how encryption can be applied in real-world scenarios.
The tasks involved using OpenSSL to perform encryption, analysing block behaviour, comparing ECB and CBC modes, and integrating encrypted data into a Git-based workflow. These activities helped bridge theoretical cryptography concepts with practical execution.

In this week I have focused on practical implementation of block cipher and encryptin modes using OpenSSL. The main aim wa to understand how does DES works at the  block level and how different modes such as ECB and CBC affect security.
This tasks involved encryption of files  analysing the ciphertext outputs and comparing  encryption behavior across different modes which has helped me connect theoretical cryptographty concepts with real command lines.

## Overview
The following tasks were completed:
-	DES encryption using OpenSSL (ECB mode).
-	Demonstration of ECB limitations.
-	Comparing of ECB and CBC modes. 
-	Encryption of a real file (README.md) 
-	Integration of encrypted output into Git

##Task 4: DES Encryption using OpenSSL (ECB Mode)
A plaintext file of exactly 24 bytes was created This confirmed the file size was 24 bytes, which matches three DES blocks (8 bytes each).First encryption was performed and then Ciphertext was viewed. This confirmed the file size was 24 bytes, which matches three DES blocks (8 bytes each)
 <img width="940" height="147" alt="image" src="https://github.com/user-attachments/assets/7a80b130-d22e-4259-acdd-cce46afc0207" />

-Screenshot showing wc -c file.txt , encryption command and xxd file.enc
DES is a block cipher that processes fixed 8-byte blocks. Since the plaintext size was exactly 24 bytes, and no padding was required. ECB mode encrypts  each block independentally.

## Task 5: DES without Padding and ECB Behaviour
I have performed DES encryption again using ECB mode with no padding and a fixed key. A small modification was made to the plaintext by changing one character in the first block.
The `xxd` output showed that only the first ciphertext block changed, while the remaining blocks stayed exactly the same. This is because ECB encrypts each block independently.

This demonstrates a major weakness of ECB mode: identical plaintext blocks always produce identical ciphertext blocks. As a result, patterns in the plaintext are preserved in the ciphertext, making ECB insecure for real-world use.

The experiment clearly shows that even a small change in one block does not affect other blocks, highlighting the lack of diffusion in ECB mode.
<img width="940" height="296" alt="image" src="https://github.com/user-attachments/assets/cafed195-89b3-4aa5-857b-978c480646a2" />
-screenshot showing all four xxd outputs

## Task 6: ECB vs CBC Mode Comparison

DES encryption was performed using both ECB and CBC modes with the same plaintext and key.

The ciphertext produced by ECB mode showed consistent block patterns because each block is encrypted independently. In contrast, the ciphertext produced using CBC mode was completely different across all blocks.

This occurs because CBC mode uses an initialization vector (IV) and combines each plaintext block with the previous ciphertext block before encryption. As a result, even identical plaintext blocks produce different ciphertext outputs.

This experiment demonstrates that CBC provides better security than ECB by removing visible patterns and introducing dependency between blocks.
<img width="940" height="188" alt="image" src="https://github.com/user-attachments/assets/16f2f772-af27-4185-a846-59e3f3f247a3" />
-screenshot showing ECB and CBC
## Task 7: Encrypting README File

A random 64-bit key was generated using OpenSSL. This key was used to encrypt the README.md file using DES in ECB mode.

The encrypted output was saved as README.bin. The file size confirmed that encryption was successful.

The encrypted file was then added to the Git repository and pushed to GitHub, demonstrating version control of encrypted data.

This task shows how encryption can be integrated into real workflows and managed using Git.

<img width="940" height="416" alt="image" src="https://github.com/user-attachments/assets/4ad4c9ed-1283-47d6-b0eb-94a81aeb4428" />
-screenshot showing key generation , encryption command and git command
<img width="940" height="291" alt="image" src="https://github.com/user-attachments/assets/5024d8ea-8981-4985-bf96-de9a3181397e" />
The screenshots shows how  encryption can be applied to real files and integrated into version control. The encrypted file was successfully stored and tracked in the repository.

## Conclusion 
This week demonstrated how cipher operate and in practice and how encryption mode affect the security system. This experiment shows that ECB mode is insecure because it exposes the patterns and CBC improves security by linking blocks together.
I have used Opessl which helped  reinforce how cryptographic operations are performed in real environments. The task also showed how encryption can be combined with development of workflow using Git.
## Reflection.
This  week I have improved my understanding  of how encryption works beyond theory. The most important learning was observing how ECB mode fails to hide the patterns which have made the concept much clear and understandable.
While working with OpenSSl required aclear and correct command lines specially dealing with key formats and compatibility issues. Thus has highlighted the importance of precision when working with security tools.
By comparing  ECB and CBC modes helped me understand why secure system avoid ECB and would prefer  some more advanced modes.
## Novel insights 
A key novel insights that I found in this week is that the strength of encryption depends not only on the algorithm but also on how it is used. Even though DES is valid cipher using it in ECB mode makes it insecure because patterns are preserved this things shows that choosing the correct mode of operation is critical.
Another novel insight that I found is that modern system restrict older algorithms like DES by default, which reflect how security standards evolve over the time. 

