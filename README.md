# CS3002 – Cryptography Concepts | CIA
## Algorithm: Hash-Generated Gronsfeld Cipher

### What is the Gronsfeld Cipher?
The Gronsfeld cipher is a polyalphabetic substitution cipher. Unlike a simple Caesar cipher (single fixed shift), it uses a **sequence of digits as the key**, where each digit shifts the corresponding plaintext letter by that amount. This makes it significantly harder to break by frequency analysis alone.

### What is DJB2?
**DJB2** is a fast, non-cryptographic hash function invented by Daniel J. Bernstein. It converts any string into a large unique integer using the formula:

```
hash_value = 5381
for each character c:
    hash_value = (hash_value × 33) + ASCII(c)
```

The multiplier `33` (implemented as `hash << 5 + hash`) distributes bits well across the hash space, giving very low collision rates for typical inputs.

### Why DJB2?
- **Unique:** Not a standard SHA/MD5 — custom and fully self-implemented, satisfying the assignment constraint.
- **Simple:** O(n) time, O(1) space — easy to implement from scratch without libraries.
- **Deterministic:** Same plaintext always produces the same key, enabling reproducible encryption.
- **Low collisions:** The 33× multiplier ensures good bit distribution across outputs.

---

## Workflow

```
Plaintext P
     │
     ▼
[DJB2 Hash] ──→ H (large integer)
     │
     ▼
H mod (10^k) ──→ Padded key string ──→ Key K = [d1, d2, ..., dk]
     │
     ▼
[Gronsfeld Encryption] ──→ Ciphertext C

To decrypt: use saved Key K with Gronsfeld Decryption ──→ Plaintext P
```

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Hash Time Complexity | O(n) where n = length of plaintext |
| Encryption/Decryption Time | O(n) |
| Space Complexity | O(k) where k = key length (fixed) |

---

## How to Run

**Requirements:** Python 3.x — no external libraries needed.

```bash
python Crypto_CIA.py
```

This runs all 4 round-trip test cases automatically.

To use the cipher in your own code:

```python
from Crypto_CIA import hash_gronsfeld_encrypt, hash_gronsfeld_decrypt

ciphertext, key = hash_gronsfeld_encrypt("YOUR MESSAGE", key_length=12)
decrypted = hash_gronsfeld_decrypt(ciphertext, key)
```

---

## Worked Examples

### Example 1 — "HELLO WORLD" (key_length = 8)

| Step | Value |
|---|---|
| Plaintext | `HELLO WORLD` |
| DJB2 Hash | `272080661459167838081` |
| Key (mod 10^8, padded) | `[6, 7, 8, 3, 8, 0, 8, 1]` |
| Encryption | H+6=N, E+7=L, L+8=T, L+3=O, O+8=W · · · |
| Ciphertext | `NLTOW WWSRK` |
| Decrypted | `HELLO WORLD` |

### Example 2 — "CRYPTOGRAPHY" (key_length = 12)

| Step | Value |
|---|---|
| Plaintext | `CRYPTOGRAPHY` |
| DJB2 Hash | `8978429637394878153329` |
| Key | `[3, 9, 4, 8, 7, 8, 1, 5, 3, 3, 2, 9]` |
| Ciphertext | `FACXAWHWDSJH` |
| Decrypted | `CRYPTOGRAPHY` |

### Example 3 — "NANDHIKA M" (key_length = 10)

| Step | Value |
|---|---|
| Plaintext | `NANDHIKA M` |
| DJB2 Hash | `8245141447016999888` |
| Key | `[7, 0, 1, 6, 9, 9, 9, 8, 8, 8]` |
| Ciphertext | `UAOJQRTI U` |
| Decrypted | `NANDHIKA M` |

### Example 4 — "THE QUICK BROWN FOX" (key_length = 20)

| Step | Value |
|---|---|
| Plaintext | `THE QUICK BROWN FOX` |
| DJB2 Hash | `382682614787349019726323614090008` |
| Key | `[4, 9, 0, 1, 9, 7, 2, 6, 3, 2, 3, 6, 1, 4, 0, 9, 0, 0, 0, 8]` |
| Ciphertext | `XQE RDPEQ ETRCO JOG` |
| Decrypted | `THE QUICK BROWN FOX` |

---

## Setbacks & Mitigations

| Limitation | Mitigation Used |
|---|---|
| Hash collisions possible | Key length of 20+ digits makes collisions practically negligible |
| DJB2 is not cryptographically secure | Suitable for this educational implementation; SHA-256 recommended for production |
| Key must be transmitted alongside ciphertext | Accepted trade-off for deterministic key generation |

---

## Files

| File | Description |
|---|---|
| `Crypto_CIA.py` | Full implementation: DJB2 hash + Gronsfeld encrypt/decrypt + test script |
| `Crypto_CIA.pdf` | Handwritten algorithm notes |
| `Crypto_CIA_prompts.pdf` | Prompts used during development |
