from cryptography.fernet import Fernet
import shlex, subprocess
import os


def generate_key():
    return Fernet.generate_key()


def load_key():
    return os.environ['CS1'].encode()


def load_pass():
    return os.environ['CS2'].encode()


def encrypt_message(msg):
    key = load_key()
    f = Fernet(key)
    encoded_msg = msg.encode()
    encrypt_msg = f.encrypt(encoded_msg)
    return encrypt_msg


def decrypt_message(msg):
    key = load_key()
    f = Fernet(key)
    decrypt_msg = f.decrypt(msg)
    return decrypt_msg.decode()
