# DJB2 HASH FUNCTION

def djb2_hash(text):
    hash_val = 5381
    for char in text:
        hash_val = ((hash_val << 5) + hash_val) + ord(char)
    return hash_val



def hash_gronsfeld_encrypt(plaintext, key_length=20):

    # Step 1: Hash generation
    h = djb2_hash(plaintext)

    # Step 2: Key extraction
    key_num = h % (10 ** key_length)
    key_str = str(key_num).zfill(key_length)
    key = [int(d) for d in key_str]

    # Step 3: Encryption
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



def run_roundtrip_test(plaintext, key_length=12, label=""):

    if label:
        print(f"  Test: {label}")
    print("\n")
    print(f"  Plaintext      : {plaintext}")

    # Encrypt
    ciphertext, key = hash_gronsfeld_encrypt(plaintext, key_length)
    print(f"  Key Length     : {key_length}")
    print(f"  DJB2 Hash      : {djb2_hash(plaintext)}")
    print(f"  Generated Key  : {key}")
    print(f"  Ciphertext     : {ciphertext}")

    # Decrypt
    decrypted = hash_gronsfeld_decrypt(ciphertext, key)
    print(f"  Decrypted      : {decrypted}")

    # Verify
    match = plaintext.upper() == decrypted.upper()
    print(f"  Round-trip OK  : {'PASS' if match else 'FAIL'}")
    return match



if __name__ == "__main__":
    
# Worked Examples 

    # Example 1 
    run_roundtrip_test("HELLO WORLD", key_length=8, label="Example 1 (key_length=8)")

    # Example 2
    run_roundtrip_test("CRYPTOGRAPHY", key_length=12, label="Example 2 (key_length=12)")

    # Example 3 
    run_roundtrip_test("NANDHIKA M", key_length=10, label="Example 3 — Name")

    # Example 4 
    run_roundtrip_test("THE QUICK BROWN FOX", key_length=20, label="Example 4 — Long plaintext")

    