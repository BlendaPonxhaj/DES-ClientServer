import socket 
from pyDes import * 


def get_predefined_key():
    return b"\x31\x41\x61\x11\x21\x31\x41\x51"


def decrypt_message(ciphertext, key):
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    decrypted_message = desi.decrypt(ciphertext)
    return decrypted_message


def encrypt_message(message, key):
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    encrypted_message = desi.encrypt(message)
    return encrypted_message



def client_program():
    host = "127.0.0.1"
    port = 5001
    key = get_predefined_key()

    print("-----------------------")
    message = input("Shkruaj nje mesazh per te derguar ne server: ")
    print("-----------------------")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        encrypted_message = encrypt_message(message,key)

        print(f'Mesazhi eshte enkriptuar "{encrypted_message}" dhe eshte derguar ne server.')
        print("--------------------")

        s.send(encrypted_message)

        # Pranon prompt-in nga serveri dhe vazhdon komunikimin e enkriptuar

        prompt = s.recv(1024)
        decrypted_prompt = decrypt_message(prompt,key)
        print(decrypted_prompt.decode())

        answer = input("")
        encrypted_answer = encrypt_message(answer,key)
        s.send(encrypted_answer)

        decrypted_data = decrypt_message(s.recv(1024),key)
        print(decrypted_data.decode())

if __name__=='__main__':
      client_program()