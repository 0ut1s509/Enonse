chaine=input("antre yon chenn karakte")
voyel=["a","e","i","o","u","y"]
i=0
nchaine=[]
for el in chaine:
   nchaine.append(el)

for i,el in enumerate(nchaine):
    if el in voyel:
        nchaine[i+1]="*"
    

print("".join(nchaine))