from dilithium_py.ml_dsa import ML_DSA_65

# Generate ML-DSA key pair
pk, sk = ML_DSA_65.keygen()

print("Key pair generated!")
print("Public key size:", len(pk), "bytes")
print("Private key size:", len(sk), "bytes")

# Message to sign
message = b"Hello, Post-Quantum World!"

# Sign the message
signature = ML_DSA_65.sign(sk, message)

print("Message signed!")
print("Signature size:", len(signature), "bytes")

# Verify the signature
valid = ML_DSA_65.verify(pk, message, signature)

print("Signature verification:", valid)

if valid:
    print("SUCCESS: ML-DSA signature is valid!")
else:
    print("ERROR: ML-DSA signature is invalid!")
