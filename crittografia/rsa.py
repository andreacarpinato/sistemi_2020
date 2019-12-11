#andrea Carpinato rsa
import random

def euclideMCD(a, b):
    while(b != 0):
        a,b=b,a%b
    return a

def trovaMCM(a,b):
	return a*b/euclideMCD(a,b)

def isPrime(n) : 
	# Corner cases 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True
	# This is checked so that we can skip 
	# middle five numbers in below loop 
	if (n % 2 == 0 or n % 3 == 0) : 
		return False
	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6
	return True

#1
p=int(input('inserisci p(n primo): \n'))
q=int(input('inserisci q(n primo): \n'))
while True:#verifico se i numeri input sono primi
    if (isPrime(p)==True):
        if(isPrime(q)==True):
            break
        else:
            q=int(input('reinserisci q(n primo): \n'))
    else:
       p=int(input('reinserisci p(n primo): \n'))  
n=p*q #2
m=int(euclideMCD(p-1,q-1))#3
print('m vale',m)
c=0
d=0
a=int(m-1)
b=2
#4 trovo c
c=random.randint(a,b)#random tra 1 e m
print('calcolo in corso...')
while True:#metodo brutale 
	print(c)
	if(euclideMCD(c,m)!=1):#se c tale che mcd(c,m)=1 esce !!cicla per falso
		c=random.randint(a,b)#random tra 1 e m
	else:
		break
#5 trovo d
d=random.randint(0,m-1)
while True:#metodo brutale,cicla per falso
	if (c*d)%m!=1:
		d=random.randint(0,m-1)
	else:
		break
#6
print('CHIAVI PUBBLICHE: n=',n,' c=',c)
print('CHIAVI PRIVATE: p=',p,' q=',q,' m=',m,' d=',d)
#7
mex=12 #il messaggio deve essere compreso tra 0 e n,perciò uso un calore basso
print('\n\nMITTENTE\nmessaggio da inviare=',mex)
mex_cod=(mex**c )%n
print('mex_codificato=',mex_cod)
print('DESTINATARIO')
mex_dec=(mex_cod**d)%n
print('decodificato=',mex_dec)

