import socket as sck



HOST = "127.0.0.1"
PORT = 1234
s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
s.connect((HOST,PORT))
N=9973
g=1567

a=int(input('inserisci a'))
while a<1 or a>N:
    a=int(input('inserisci a'))
A = (g**a)%N

#invio numero all'host con cui scambiare la chiave 
s.send(str(A).encode())
data = s.recv(4096)

#ricezione numero dall'altro host 
print("received -->" + str(data))
B = int(data.decode())

#chiusura socket
s.close()

#calcolo numero finale
k = (B**a)%N