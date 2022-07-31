sekans=[0,1,2,3,4]
nsekans=[]

for i,el in enumerate(sekans):
    if i==0:
        sekans=sekans[::-1]
        
    if i==1:
        sekans=list(reversed(sekans[0:-1]))+sekans[-1:]
    if i==2:
        sekans=list(reversed(sekans[0:-2]))+sekans[-2:]
    if i==3:
        sekans=list(reversed(sekans[0:-3]))+sekans[-3:]
        nsekans=sekans

for i,el in enumerate(nsekans):
    if i==1:
        print("(",el,", ",i,")")



    