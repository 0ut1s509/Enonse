def cap(mo):
    mo=mo.lower()
    lis=[]
    for el in mo:
        lis.append(el[0].upper()+el[1:])
    print (lis)

x=cap("Ayiti SE Yon Bel PEyi")
        