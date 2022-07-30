from operator import mul
chaine="5 45 123 12"
chaine=chaine.split()

multi=1

for el in chaine:
    multi=multi*int(el)

print(multi)
    