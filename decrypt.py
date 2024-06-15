from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from io import BytesIO
import base64
import zlib
import os

def decrypt(encrypted, private_key):
    try:
        encrypted_bytes = BytesIO(base64.decodebytes(encrypted))
        
        pubkey_length = 450  # Approx length for a 2048-bit key in PEM format
        public_key = encrypted_bytes.read(pubkey_length)
        encrypted_session_key = encrypted_bytes.read(256)  # RSA 2048-bit key size in bytes
        nonce = encrypted_bytes.read(16)
        tag = encrypted_bytes.read(16)
        ciphertext = encrypted_bytes.read()
        
        rsakey = RSA.import_key(private_key)
        cipher_rsa = PKCS1_OAEP.new(rsakey)
        session_key = cipher_rsa.decrypt(encrypted_session_key)
        
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        decrypted = cipher_aes.decrypt_and_verify(ciphertext, tag)
        plaintext = zlib.decompress(decrypted)
        return plaintext
    except (ValueError, KeyError) as e:
        print(f"Decryption error: {e}")
        return None

def decrypt_file(input_file, private_key):
    try:
        with open(input_file, 'rb') as f:
            encrypted_message = f.read()
        
        decrypted_message = decrypt(encrypted_message, private_key)
        if decrypted_message is None:
            raise ValueError("Decryption failed. Invalid key.")
        
        output_file = input_file.replace('.enc', '')
        with open(output_file, 'wb') as f:
            f.write(decrypted_message)
        
        os.remove(input_file)
        print(f'Decrypted {input_file} to {output_file}')
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

def decrypt_directory(directory, private_key_file):
    try:
        if not os.path.exists(private_key_file):
            raise FileNotFoundError(f"Private key file '{private_key_file}' not found.")
        
        with open(private_key_file, 'rb') as f:
            private_key = f.read()
        
        for root, _, files in os.walk(directory):
            for filename in files:
                if filename.endswith('.enc'):
                    file_path = os.path.join(root, filename)
                    if os.path.isfile(file_path):
                        try:
                            decrypt_file(file_path, private_key)
                        except Exception as e:
                            print(f"Skipping {file_path}: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

if __name__ == "__main__":
    decrypt_directory('.', 'key.pri')
