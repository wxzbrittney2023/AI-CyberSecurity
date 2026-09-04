from kyber_py.ml_kem import ML_KEM_768

# Generate ML-KEM key pair
ek, dk = ML_KEM_768.keygen()

print("Key pair generated!")
print("Encapsulation key size:", len(ek), "bytes")
print("Decapsulation key size:", len(dk), "bytes")

# Encapsulate
key1, ciphertext = ML_KEM_768.encaps(ek)

print("Encapsulation completed!")
print("Ciphertext size:", len(ciphertext), "bytes")
print("Shared secret size:", len(key1), "bytes")

# Decapsulate
key2 = ML_KEM_768.decaps(dk, ciphertext)

print("Decapsulation completed!")

# Check whether both shared secrets are identical
if key1 == key2:
    print("SUCCESS: Both parties have the same shared secret!")
else:
    print("ERROR: Shared secrets are different!")