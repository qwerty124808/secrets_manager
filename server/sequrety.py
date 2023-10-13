import base64
import hashlib
import os
import re
from typing import Tuple

from Crypto.Cipher import DES


class StandardPBEStringEncryptor:
    def __init__(
        self,
        salt_size: int = 8,
        iterations: int = 1000,
    ):
        self.salt_size = salt_size
        self.iterations = iterations

    def get_derived_key(
        self,
        password: bytes,
        salt: bytes,
        count: int,
    ) -> Tuple[bytes, bytes]:
        key = password + salt
        for i in range(count):
            m = hashlib.md5(key)
            key = m.digest()
        return key[:8], key[8:]

    def decrypt(self, msg: str, password: str) -> str:
        """ Расшифровка """
        password_bytes = password.encode('utf-8')
        msg_bytes = base64.b64decode(msg)
        salt = msg_bytes[: self.salt_size]
        enc_text = msg_bytes[self.salt_size :]
        (dk, iv) = self.get_derived_key(password_bytes, salt, self.iterations)
        crypter = DES.new(dk, DES.MODE_CBC, iv)
        text = crypter.decrypt(enc_text)
        return re.sub(r'[\x01-\x08]', '', text.decode())

    def encrypt(self, msg: str, password: str) -> str:
        """ Шифровка PBEWithMD5AndDES """
        password_bytes = password.encode('utf-8')
        salt = os.urandom(self.salt_size)
        pad_num = self.salt_size - (len(msg) % self.salt_size)
        for i in range(pad_num):
            msg += chr(pad_num)
        (dk, iv) = self.get_derived_key(password_bytes, salt, self.iterations)
        crypter = DES.new(dk, DES.MODE_CBC, iv)
        enc_text = crypter.encrypt(msg.encode('utf-8'))
        return base64.b64encode(salt + enc_text).decode('utf-8')


encryptor = StandardPBEStringEncryptor()


def encrypt(
    msg: str,
    password: str,
) -> str:
    return encryptor.encrypt(msg, password)


def decrypt(
    msg: str,
    password: str
) -> str:
    return encryptor.decrypt(msg, password)

