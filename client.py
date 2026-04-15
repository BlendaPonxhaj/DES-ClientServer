import socket
from pyDes import des, ECB, PAD_PKCS5


def get_predefined_key():
    return b"\x31\x41\x61\x11\x21\x31\x41\x51"


def encrypt_message(message: str, key: bytes) -> bytes:
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    return desi.encrypt(message.encode("utf-8"))


def decrypt_message(ciphertext: bytes, key: bytes) -> str:
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    return desi.decrypt(ciphertext).decode("utf-8")


def client_program() -> None:
    host = "127.0.0.1"
    port = 5001
    key = get_predefined_key()

    print("-----------------------")
    message = input("Shkruaj nje mesazh per te derguar ne server: ")
    print("-----------------------")

    encrypted_message = encrypt_message(message, key)
    print(f"Mesazhi eshte enkriptuar: {encrypted_message!r} dhe eshte derguar ne server")
    print("--------------------")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(encrypted_message)


if __name__ == "__main__":
    client_program()