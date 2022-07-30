a=int(input("antre yon antye : "))
b=int(input("antre yon lot antye : "))

if (a>b):
    res=(a/b)/2
    res=int(res)
    
    print("a = ",a,"\t\t\t",res)
    print("b = ",b,"\n")
elif(a<b):
    res=(b/a)/2
    res=int(res)
    print("Resultat : ",res)
    print("a = ",a,"\t\t\t",res)
    print("b = ",b,"\n")
else:
    res=(b/a)/2
    print("a = ",a,"\t\t\t",res)
    print("b = ",b,"\n")
