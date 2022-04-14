import socket
import elgamal
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
client.connect(('localhost', 1002))  # 127.0.0.1

msg = input("msg: ")
q=elgamal.q
h=elgamal.h
g=elgamal.g
ct,p=elgamal.enc(msg,q,h,g)
print("Sending encrypted msg...")
client.send(pickle.dumps(ct))
print("msg sent.")
print("Encrypted msg=",ct)

client.close()