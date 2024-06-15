# File Encryption and Decryption

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


