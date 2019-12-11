numeri=range(0,26)
alfanum={}
numalf={}
parola_crittografata=[]
chiave_crittografata=[]


for k in numeri: #creazione dizionario alfa-numerico
    x=chr(k+65)
    numalf[k]= x 
    alfanum[x]=k
print(alfanum)
print(numalf)
# utente inserisce parola e chiave
chiave=input("Inserisci la chiave:")
chiave=chiave.upper()
phrase = input("Iserisci il  messaggio: ") 
phrase=phrase.upper()
if len(chiave) <len(phrase):
    print('chiave troppo corta')
else:
    parolaChiara=[]
    for i,c in enumerate(list(phrase)):
       x= (alfanum[c]-alfanum[chiave[i]]+26)%26
       parolaChiara.append(numalf[x]) 
    print(''.join(parolaChiara))

    