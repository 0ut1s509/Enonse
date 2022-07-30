chaine="web-insecure;34829sjdfnsj32984madsdkj"

chaine=chaine.split(";")
for i, el in enumerate(chaine):
    if i==0:
        chaine.remove(el)
chaine="".join(chaine)

print(chaine)