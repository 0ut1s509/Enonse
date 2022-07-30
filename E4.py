a=3
b=4


enteval=range(1,30)
print("a = ",a,"\nb = ",b)
print("enteval ant 1 jiska 30\n")

multiple_a_and_b=[]
multiple_a_not_b=[]
multiple_b_not_a=[]
not_multiple_a_and_b=[]
for nb in enteval:
    if (nb%a==0) and (nb%b!=0):
        multiple_a_not_b.append(nb)
    if (nb%a!=0) and (nb % b) == 0:
        multiple_b_not_a.append(nb)
    if (nb%a==0) and (nb%b==0):
        multiple_a_and_b.append(nb)
    if (nb%a!=0) and (nb%b!=0):
        not_multiple_a_and_b.append(nb)



print("Miltip a, men ki pa miltip b : ",multiple_a_not_b," nonb lan se : ",len(multiple_a_not_b))
print("Militp b, men ki pa miltip a : ",multiple_b_not_a," nonb lan se : ",len(multiple_b_not_a))
print("Miltip b ak a : ",multiple_a_and_b," nonb lan se : ",len(multiple_a_and_b))
print("ki pa miltip ni a ni b : ",not_multiple_a_and_b," nonb lan se : ",len(not_multiple_a_and_b))



