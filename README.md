# Crypto Post-Quantum Encryption Lib

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Lattice Crypto](https://img.shields.io/badge/Lattice_Crypto-LWE-green.svg)](https://en.wikipedia.org/wiki/Learning_with_errors)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **post-quantum cryptography library** implementing lattice-based encryption schemes. This repository features a toy implementation of the **Learning With Errors (LWE)** public-key cryptosystem, demonstrating resistance to quantum computer attacks.

> **⚠️ WARNING**: This implementation is for educational and research purposes only. Do not use for securing real-world sensitive data. Parameters are chosen for correctness, not 128-bit security.

## 🚀 Features

- **LWE Encryption**: Public-key encryption based on the hardness of the LWE problem.
- **Key Generation**: Generation of secret and public keys using matrix operations.
- **noisy Arithmetic**: Implementation of modulo arithmetic with error distributions.
- **Bit-level Encryption**: Encrypts messages bit-by-bit (multi-bit support via vectors).

## 📁 Project Structure

```
crypto-post-quantum-encryption-lib/
├── src/
│   ├── lattice_crypt.py  # LWE Core Logic
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/crypto-post-quantum-encryption-lib.git

# Install
pip install -r requirements.txt

# Run Demo
python src/main.py --message "Hello Quantum World"
```

## 📄 License

MIT License
