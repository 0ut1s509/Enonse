import string
'''def kripte(param1):
    param=param1
    param=param.replace(" ", "")
    x=None
    w=""
    for el in param.upper():
        
        x=string.ascii_uppercase.index(el)
        x=str(x)
        x+="-"
        w+=x
        


    
  
    


    return w[0:-1]
x=kripte("alo alo")
print(x) '''

nchaine=""
nchaine1=[]
def dekripte(chaine):
    chaine=chaine.upper()
    for el in chaine.split() :
        if el[0]==">":
            n0=string.ascii_uppercase.index(el[-1:])
            n1=string.ascii_uppercase[n0+int(el[1:-1])]
            nchaine1.append(n1)

        if el[0]=="<":
            n0=string.ascii_uppercase.index(el[-1:])
            n1=string.ascii_uppercase[n0-int(el[1:-1])]
            nchaine1.append(n1)
    print(chaine," ap bay : ","".join(nchaine1))        

        
antre=input("Antre sekans karakte a : ")
dekripte(antre)


