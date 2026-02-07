import argparse
import time
from src.lattice_crypt import LWESystem

def main():
    parser = argparse.ArgumentParser(description="Post-Quantum LWE Encryption Demo")
    parser.add_argument("--message", default="Secret Data", help="Message to encrypt")
    
    args = parser.parse_args()
    
    print("--- Post-Quantum Cryptography Demo (LWE) ---")
    
    # Initialize System
    print("Initializing LWE Lattice parameters (n=128, q=2048)...")
    lwe = LWESystem()
    
    # Key Generation
    start = time.time()
    lwe.generate_keys()
    print(f"Key Generation took: {time.time() - start:.4f}s")
    
    # Encryption
    print(f"\nEncrypting: '{args.message}'")
    start = time.time()
    ciphertext = lwe.encrypt_message(args.message)
    print(f"Encryption took: {time.time() - start:.4f}s")
    print(f"Ciphertext size: {len(ciphertext)} pairs of (vector, scalar)")
    
    # Decryption
    print(f"\nDecrypting...")
    start = time.time()
    decrypted = lwe.decrypt_message(ciphertext)
    print(f"Decryption took: {time.time() - start:.4f}s")
    
    print(f"\nResult: '{decrypted}'")
    assert decrypted == args.message, "Decryption failed!"
    print("Verification Successful ✅")

if __name__ == "__main__":
    main()
