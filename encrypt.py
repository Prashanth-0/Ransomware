from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
import base64
import zlib
import os

def get_rsa_cipher(key_file):
    try:
        with open(key_file, 'rb') as f:
            key = f.read()
            print(f"{key_file} content loaded successfully.")
        rsakey = RSA.import_key(key)
        return PKCS1_OAEP.new(rsakey), rsakey.size_in_bytes()
    except Exception as e:
        print(f"Error loading RSA key ({key_file}): {e}")
        raise

def encrypt(plaintext, pubkey_file):
    try:
        compressed_text = zlib.compress(plaintext)
        session_key = get_random_bytes(16)
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(compressed_text)
        cipher_rsa, _ = get_rsa_cipher(pubkey_file)
        encrypted_session_key = cipher_rsa.encrypt(session_key)
        with open(pubkey_file, 'rb') as f:
            pubkey_content = f.read()
        msg_payload = pubkey_content + encrypted_session_key + cipher_aes.nonce + tag + ciphertext
        encrypted = base64.encodebytes(msg_payload)
        return encrypted
    except Exception as e:
        print(f"Encryption error: {e}")
        raise

def encrypt_file(input_file, pubkey_file):
    try:
        with open(input_file, 'rb') as f:
            plaintext = f.read()
        encrypted_message = encrypt(plaintext, pubkey_file)
        with open(input_file + '.enc', 'wb') as f:
            f.write(encrypted_message)
        os.remove(input_file)
        print(f'Encrypted {input_file} to {input_file}.enc')
    except Exception as e:
        print(f"Error encrypting file {input_file}: {e}")
        raise

def encrypt_directory(directory, pubkey_file, exclude_files):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename in exclude_files or filename.endswith('.enc'):
                print(f"Skipping {filename}")
                continue
            file_path = os.path.join(root, filename)
            try:
                encrypt_file(file_path, pubkey_file)
            except Exception as e:
                print(f"Skipping {file_path}: {e}")

if __name__ == "__main__":
    exclude_files = ['key.pub', 'key.pri', 'encrypt.py', 'decrypt.py']
    encrypt_directory('.', 'key.pub', exclude_files)
