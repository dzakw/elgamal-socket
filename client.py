import socket
import elgamal
import pickle

client = socket.socket() #socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP


# the ip address or hostname of the server, the receiver
host = socket.gethostname()
# the port, let's use 5001
port = 1024

print(f"[+] Connecting to {host}:{port}")
client.connect((host, port))  # 127.0.0.1
print("[+] Connected.")

msg = input("[+] msg: ")
q=elgamal.q
h=elgamal.h
g=elgamal.g
ct,p=elgamal.enc(msg,q,h,g)
print("[+] Sending encrypted msg...")
client.send(pickle.dumps(ct))
print("[+] msg sent.")
print("[+] Encrypted msg=",ct)
print("[+] Connection closed.")

client.close()