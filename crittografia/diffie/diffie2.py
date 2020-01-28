import socket as sck



HOST = "127.0.0.1"
PORT = 1234
s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
s.connect((HOST,PORT))
N=9973
g=1567

b=int(input('inserisci b'))
while int(b)<1 or int(b)>N:
    b=int(input('inserisci b'))
B = (g**b)%N

conn, addr = s.accept()
print("connected to " + str(addr))

#ricezione dati e conversione
data = conn.recv(4096)
print("received: --> " + str(data))
A = int(data.decode())

#invio dati calcolati
conn.send(str(B).encode())
conn.close()

#calcolo del risultato finale
k=(A**b)%N
print(f"il numero è {k}")