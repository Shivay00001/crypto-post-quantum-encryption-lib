"""Smoke test for crypto-post-quantum-encryption-lib: LWE encrypt/decrypt roundtrip."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.lattice_crypt import LWESystem


def main():
    lwe = LWESystem()
    pub, sec = lwe.generate_keys()
    assert pub is not None and sec is not None

    for bit in (0, 1):
        ct = lwe.encrypt_bit(bit, pub)
        assert lwe.decrypt_bit(ct, sec) == bit, f"bit roundtrip failed for {bit}"

    msg = "Hi"
    ct = lwe.encrypt_message(msg)
    assert lwe.decrypt_message(ct) == msg

    print("smoke OK: generate_keys, encrypt/decrypt bit, message roundtrip")


if __name__ == "__main__":
    main()
