def addi(chaine):
    somme=0
    for el in chaine:
        somme+=int(el)
    return somme

chaine ="122 23 40"
chaine=chaine.split()
nchaine=[]
som=0   
prod=1





for el in chaine:
    som=addi(el)
    nchaine.append(som)

for el in nchaine:
    prod*=el

print("Resultat : ",prod)
    






