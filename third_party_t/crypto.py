from Crypto.PublicKey import RSA

# 生成密钥对
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# 公钥加密、私钥解密
def encrypt_with_public_key(plaintext, public_key):
    rsa_key = RSA.import_key(public_key)
    ciphertext = rsa_key.encrypt(plaintext.encode(), None)[0]
    return ciphertext

def decrypt_with_private_key(ciphertext, private_key):
    rsa_key = RSA.import_key(private_key)
    plaintext = rsa_key.decrypt(ciphertext)
    return plaintext.decode()

# 测试
message = "Hello, world!"

# 公钥加密、私钥解密
encrypted_message = encrypt_with_public_key(message, public_key)
decrypted_message = decrypt_with_private_key(encrypted_message, private_key)

print("公钥加密、私钥解密")
print("原始消息:", message)
print("加密后:", encrypted_message)
print("解密后:", decrypted_message)
