from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# 生成密钥对
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# 私钥加密、公钥认证
def encrypt_with_private_key(plaintext, private_key):
    rsa_key = RSA.import_key(private_key)
    signer = pkcs1_15.new(rsa_key)
    digest = SHA256.new(plaintext.encode())
    signature = signer.sign(digest)
    return signature

def encrypt_with_private_key_t(plaintext, private_key):
    rsa_key = RSA.import_key(private_key)
    signer = pkcs1_15.new(rsa_key)
    digest = SHA256.new(plaintext.encode())
    signature = signer.sign(digest)
    return signature

def verify_with_public_key(plaintext, signature, public_key):
    rsa_key = RSA.import_key(public_key)
    verifier = pkcs1_15.new(rsa_key)
    digest = SHA256.new(plaintext.encode())
    try:
        verifier.verify(digest, signature)
        return True
    except (ValueError, TypeError):
        return False

# 测试
message = "Hello, world!"

# 私钥加密、公钥认证
signature = encrypt_with_private_key(message, private_key)
verification_result = verify_with_public_key(message, signature, public_key)

print("\n私钥加密、公钥认证")
print("原始消息:", message)
print("数字签名:", signature)
print("验证结果:", verification_result)
