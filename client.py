import socket from pyDes import *

def get_predefined_key():
    return b"\x31\x41\x61\x11\x21\x31\x41\x51"

    def encrypt_message(message,key):
        desi=des(key,ECB, pad=None, padmode=PAD_PKCS5)
        encrypted_message=desi.encrypt(message)
        return encrypted_message

    def decrypt_message(ciphertext,key):
        desi=des(key,ECB,pad=None,padmode=PAD_PKCS5)
        decrypted_message=desi.decrypt(ciphertext)
        return decrypt_message    