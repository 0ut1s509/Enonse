def cap(mo):
    mo=mo.lower()
    capi=mo.split()
    capi1=[]
    
    for el in capi:
        capi1.append(el[0].upper()+el[1:])
    capi1=" ".join(capi1)
    print(capi1)
       
cap("Ayiti se yon BEl PEyi")