#Everythinng  is  assumedin the code.
import random

def generate_private_key(p):
    return random.randint(2, p - 2)

def compute_public_key(g, private_key, p):
    return pow(g, private_key, p)

def compute_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)

def diffie_hellman():
    # Prime number (p) and primitive root (g) - Publicly shared values
    p = 23  # Example small prime number
    g = 5   # Example primitive root modulo p
    
    # Alice and Bob generate their private keys
    private_key_Alice = generate_private_key(p)
    private_key_Bob = generate_private_key(p)
    
    # Compute public keys
    public_key_Alice = compute_public_key(g, private_key_Alice, p)
    public_key_Bob = compute_public_key(g, private_key_Bob, p)
    
    # Compute shared secret keys
    shared_secret_Alice = compute_shared_secret(public_key_Bob, private_key_Alice, p)
    shared_secret_Bob = compute_shared_secret(public_key_Alice, private_key_Bob, p)
    
    print(f"Prime (p): {p}, Primitive Root (g): {g}")
    print(f"Alice's Private Key: {private_key_Alice}")
    print(f"Bob's Private Key: {private_key_Bob}")
    print(f"Alice's Public Key: {public_key_Alice}")
    print(f"Bob's Public Key: {public_key_Bob}")
    print(f"Shared Secret (Alice's Computation): {shared_secret_Alice}")
    print(f"Shared Secret (Bob's Computation): {shared_secret_Bob}")
    
    assert shared_secret_Alice == shared_secret_Bob, "Key exchange failed!"
    print("Key exchange successful! Shared secret established.")

if __name__ == "__main__":
    diffie_hellman()
