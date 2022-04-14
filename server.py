import socket
import elgamal
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
server.bind(('localhost', 1002))  # 127.0.0.1
server.listen()

client_socket, client_address = server.accept()

ct = pickle.loads(client_socket.recv(2048))
print("Receiving text...")
print("encrypted message: ", end="")
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
print("decrypted message: ", end="")
print(lts(pt))

client_socket.close()

""""
dec(ct,p,key,q)
pt=dec(ct,p,key,q)
d_msg=''.join(pt)
print("Decryted msg=",d_msg)
"""