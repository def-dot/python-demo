from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


class CryptoGraphyT:
    def __init__(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
        self.public_key = self.private_key.public_key()
        self.data = b"hello world"

    def private_sign(self):
        sign = self.private_key.sign(
            self.data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return sign

    def public_verify(self, sign):
        try:
            self.public_key.verify(
                sign,
                self.data,
                padding.PSS(
                    padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            print("success, sign is valid!")
        except Exception as e:
            print("fail, sign is invalid!")


if __name__ == '__main__':
    crypto = CryptoGraphyT()
    sign = crypto.private_sign()
    crypto.public_verify(sign)
