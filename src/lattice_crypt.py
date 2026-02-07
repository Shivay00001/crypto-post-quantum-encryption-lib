import numpy as np
import secrets

class LWESystem:
    def __init__(self, n=128, q=2048, sigma=2.0):
        self.n = n          # Dimension of the lattice
        self.q = q          # Modulus
        self.sigma = sigma  # Error standard deviation
        self.m = 2 * n      # Number of samples (public key size factor)

    def generate_keys(self):
        """Generates Secret Key (s) and Public Key (A, b)."""
        # Secret key s: vector of size n, elements in Z_q
        self.s = np.random.randint(0, self.q, self.n)
        
        # Public key A: matrix m x n
        self.A = np.random.randint(0, self.q, (self.m, self.n))
        
        # Error vector e: small noise
        e = np.random.normal(0, self.sigma, self.m).astype(int)
        
        # Public key b = As + e (mod q)
        self.b = (self.A @ self.s + e) % self.q
        
        return (self.A, self.b), self.s

    def encrypt_bit(self, bit: int, pub_key):
        """Encrypts a single bit (0 or 1)."""
        A, b = pub_key
        
        # Sample random vector r (subset sum selector) - just using binary here for Regev style (simplified)
        # Actually usually r is binary vector of size m in some schemes, or small vector.
        # Let's use simple subset sum: choose random subset of rows.
        # Efficient way: r is a binary vector of size m
        r = np.random.randint(0, 2, self.m)
        
        # u = A^T * r (mod q)
        u = (self.A.T @ r) % self.q
        
        # v = b^T * r - bit * (q/2) (mod q) ... wait, encoding is + bit * q/2
        # v' = b.r + message_encoding + noise? 
        # Standard LWE Enc:
        # u = Σ A_i (for i in subset)
        # v = Σ b_i + M * floor(q/2)
        
        v_pre = np.dot(self.b, r) % self.q
        encoding = int(bit * (self.q // 2))
        v = (v_pre + encoding) % self.q
        
        return (u, v)

    def decrypt_bit(self, ciphertext, sec_key):
        """Decrypts a single bit."""
        u, v = ciphertext
        s = sec_key
        
        # Decryption: v - s.u 
        # = (b.r + M*q/2) - s.(A^T.r)
        # = ((As+e).r + M*q/2) - s.A^T.r
        # = s.A^T.r + e.r + M*q/2 - s.A^T.r
        # = e.r + M*q/2
        # If e.r is small, we recover M.
        
        decrypted_val = (v - np.dot(s, u)) % self.q
        
        # If result is close to 0 -> 0, close to q/2 -> 1
        distance_to_0 = min(decrypted_val, self.q - decrypted_val)
        distance_to_half = abs(decrypted_val - (self.q // 2))
        
        if distance_to_0 < distance_to_half:
            return 0
        else:
            return 1

    def encrypt_message(self, message: str):
        """Encrypts a string message."""
        bits = ''.join(format(ord(c), '08b') for c in message)
        ciphertexts = []
        for b in bits:
            ciphertexts.append(self.encrypt_bit(int(b), (self.A, self.b)))
        return ciphertexts

    def decrypt_message(self, ciphertexts):
        """Decrypts a list of ciphertexts to string."""
        decrypted_bits = []
        for ct in ciphertexts:
            decrypted_bits.append(str(self.decrypt_bit(ct, self.s)))
        
        bit_string = ''.join(decrypted_bits)
        chars = []
        for i in range(0, len(bit_string), 8):
            byte = bit_string[i:i+8]
            chars.append(chr(int(byte, 2)))
        return ''.join(chars)
