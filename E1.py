ip=input("Antre adresse ip a : ")
ip=ip.replace(".",)
nchaine=[]
pot=0
for el in ip:
    nchaine.append(el)

for el in nchaine:
    pot=pot+int(el)

print("pot ki ouvri a se : ",pot)