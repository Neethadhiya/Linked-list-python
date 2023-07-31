dec=[1,9,2,1,2,3,4,5]
count=0
for i in range(len(dec)):
    for j in range(i+1,len(dec)):
        if dec[i]>dec[j]:
            temp=dec[i]
            dec[i]=dec[j]
            dec[j]=temp
unique=[]            
    
    

