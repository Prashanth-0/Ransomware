# File Encryption and Decryption

![Downloads](https://img.shields.io/pypi/dm/Ransomware)


This project provides scripts to encrypt and decrypt files using RSA and AES encryption. The scripts recursively traverse directories, encrypting or decrypting all files except the script files and the key files.

## Requirements

- Python 3.6 or later
- `pycryptodome` library

## Installation

### Windows

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Prashanth-0/Ransomware.git
    ```
    ```
    cd Ransomware
    ```


### Linux / MacOS

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Prashanth-0/Ransomware.git
    ```
    ```
    cd Ransomware
    ```

3. **Install the required library**:

    ```bash
    pip install pycryptodome
    ```

## Usage

### Key Generation

To generate a new pair of RSA keys, run:

```bash
python3 generate_keys.py
```
This will create two files:
`key.pub`and `key.pri`.

### Encryption

To encrypt all files in the current directory and its subdirectories, run:

```
python encrypt.py
```

This script will encrypt all files except the script files and the key files, and will create encrypted files with a `.enc` extension.


### Decryption

To decrypt all encrypted files in the current directory and its subdirectories, run:

```
python decrypt.py
```

This script will decrypt all files with a `.enc` extension using the `key.pri` file.


---

### Disclaimer
this repository is provided "as is" without any warranties, express or implied. Use it at your own risk. The authors and contributors are not responsible for any damage, data loss, or other issues arising from the use of this software. Ensure you understand the encryption and decryption processes before using these scripts in a production environment. Always back up your data before performing encryption or decryption operations.

