enteval=range(1,40)
print("enteval de 1 jiska 40\n")
nonb_pe=[]
for el in enteval:
    if el % 2==0:
        nonb_pe.append(str(el))
nonb_pe=" ".join(nonb_pe)
print("nonb ki pe yo se : ",nonb_pe)
