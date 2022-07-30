tablo_nonb=[1,2,3,4,5,6,7]
pi_gran=tablo_nonb[0]
pi_piti=tablo_nonb[0]

for el in tablo_nonb:
    if el>pi_gran:
        pi_gran=el
    if el<pi_piti:
        pi_piti=el
print("pi gran nonb lan se : ",pi_gran,"\nPi piti a se : ",pi_piti)
