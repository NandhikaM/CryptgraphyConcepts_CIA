def djb2_hash(text):
    """DJB2 hash function - converts string to large integer"""
    hash_val = 5381
    for char in text:
        hash_val = ((hash_val << 5) + hash_val) + ord(char)
    return hash_val

def hash_gronsfeld_encrypt(plaintext, key_length=20):
    """Generate key from hash and encrypt using Gronsfeld cipher"""
    # 1. Generate hash from plaintext
    h = djb2_hash(plaintext)
    
    # 2. Extract numeric key (collision-resistant: longer key)
    key_num = h % (10 ** key_length)
    key_str = str(key_num).zfill(key_length)
    key = [int(d) for d in key_str]
    
    # 3. Encrypt
    ciphertext = ""
    key_idx = 0
    for char in plaintext.upper():
        if char.isalpha():
            base = ord('A')
            pos = ord(char) - base
            shift = key[key_idx % len(key)]
            new_pos = (pos + shift) % 26
            ciphertext += chr(base + new_pos)
            key_idx += 1
        else:
            ciphertext += char
    
    return ciphertext, key

def hash_gronsfeld_decrypt(ciphertext, key):
    """Decrypt using saved numeric key"""
    plaintext = ""
    key_idx = 0
    for char in ciphertext.upper():
        if char.isalpha():
            base = ord('A')
            pos = ord(char) - base
            shift = key[key_idx % len(key)]
            new_pos = (pos - shift + 26) % 26
            plaintext += chr(base + new_pos)
            key_idx += 1
        else:
            plaintext += char
    return plaintext

# ==================== DEMO ====================
if __name__ == "__main__":
    # Test cases
    plaintexts = ["HELLO WORLD", "CRYPTOGRAPHY"]
    
    for pt in plaintexts:
        print(f"Plaintext: {pt}")
        
        # Encrypt
        ct, key = hash_gronsfeld_encrypt(pt, key_length=12)
        print(f"Ciphertext: {ct}")
        print(f"Generated Key: {key}")
        
        # Decrypt
        decrypted = hash_gronsfeld_decrypt(ct, key)
        print(f"Decrypted: {decrypted}")
    
    

