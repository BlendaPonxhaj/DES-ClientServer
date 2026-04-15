import socket from pyDes import * 


def get_predefined_key():
    return b"\x31\x41\x61\x11\x21\x31\x41\x51"


def encrypt_message(message, key):
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    encrypted_message=desi.encrypt(message)
    return encrypted_message


def decrypt_message(ciphertext, key):
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    decrypted_message=desi.decrypt(ciphertext)
    return decrypted_message


def client_program():
    host = "127.0.0.1"
    port = 5001
    key = get_predefined_key()

    print("-----------------------")
    message = input("Shkruaj nje mesazh per te derguar ne server: ")
    print("-----------------------")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        encrypted_message=encrypt_message(message,key)

        print(f'Mesazhi eshte enkriptuar "(encrypted_message)"dhe eshte derguar ne server.')
        print("--------------------")

        s.send(encrypted_message)