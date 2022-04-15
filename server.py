import socket
import elgamal
import pickle


SERVER_HOST = "0.0.0.0"
SERVER_PORT = 1024

server = socket.socket() #socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
server.bind((SERVER_HOST, SERVER_PORT))  # 127.0.0.1
server.listen()
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

client_socket, client_address = server.accept()
print(f"[+] {client_address} is connected.")

ct = pickle.loads(client_socket.recv(2048))
print("[+] Receiving text...")
print("[+] encrypted message: ", end="")
print(ct)

def lts(s): 
    # initialize an empty string
    str1 = "" 
    # return string  
    return (str1.join(s))

p=elgamal.p
key=elgamal.key
q=elgamal.q
pt=elgamal.dec(ct,p,key,q)
print("[+] decrypted message: ", end="")
print(lts(pt))

client_socket.close()