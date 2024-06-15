from Cryptodome.PublicKey import RSA

def generate_keys():
    new_key = RSA.generate(2048)
    private_key = new_key.exportKey()
    public_key = new_key.publickey().exportKey()

    with open('key.pri', 'wb') as f:
        f.write(private_key)

    with open('key.pub', 'wb') as f:
        f.write(public_key)
    print("RSA keys generated.")

if __name__ == "__main__":
    generate_keys()
    
