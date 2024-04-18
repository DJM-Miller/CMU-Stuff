from cryptography.fernet import Fernet
import base64

# Generate a key
key = Fernet.generate_key()

# Instantiate a Fernet symmetric key cipher with the generated key
cipher_suite = Fernet(key)

# Your message to encrypt
message = b"Hello World!"

# Encrypt the message
cipher_text = cipher_suite.encrypt(message)

print("Encrypted:", cipher_text.decode('utf-8'))

# Decrypt the message
decrypted_text = cipher_suite.decrypt(cipher_text)

print("Decrypted:", decrypted_text.decode('utf-8'))

print("Symmetric key:", key.decode('utf-8'))
