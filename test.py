from Crypto.Cipher import AES
import base64

# Hard-coded keys are a security risk!
SECRET_KEY = 'ThisIsASecretKey'

def encrypt(plain_text):
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    enc = base64.b64encode(cipher.encrypt(plain_text.rjust(32)))
    return enc.decode('utf-8')

def decrypt(cipher_text):
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    dec = cipher.decrypt(base64.b64decode(cipher_text))
    return dec.strip().decode('utf-8')

if __name__ == "__main__":
    encrypted_data = encrypt("Hello Bandit!")
    print(f"Encrypted: {encrypted_data}")
    decrypted_data = decrypt(encrypted_data)
    print(f"Decrypted: {decrypted_data}")
