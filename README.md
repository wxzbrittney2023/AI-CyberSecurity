# AI-CyberSecurity

Learning and exploring Cybersecurity, Artificial Intelligence, and Post-Quantum Cryptography.

## Project Overview

This project demonstrates two post-quantum cryptography algorithms:

ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism)
ML-DSA (Module-Lattice-Based Digital Signature Algorithm)

The implementations are developed in Python for educational purposes.

## ML-KEM

ML-KEM is a post-quantum key encapsulation mechanism designed to establish a shared secret between two parties.

This project uses **ML-KEM-768**.

### ML-KEM Test Results

| Parameter           | Result     |
| Public key size     | 1184 bytes |
| Private key size    | 2400 bytes |
| Ciphertext size     | 1088 bytes |
| Shared secret size  | 32 bytes   |
| Key agreement       | Successful |

The test program generates a key pair, performs encapsulation and decapsulation, and verifies that both parties obtain the same shared secret.

## ML-DSA

ML-DSA is a post-quantum digital signature algorithm used to create and verify digital signatures.

This project uses **ML-DSA-65**.

### ML-DSA Test Results

| Parameter              | Result     |
| Public key size        | 1952 bytes |
| Private key size       | 4032 bytes |
| Signature size         | 3309 bytes |
| Signature verification | Successful |

The test program generates an ML-DSA key pair, signs a message, and verifies the digital signature.

## Installation

Create a Python virtual environment:

```bash
python3 -m venv .venv