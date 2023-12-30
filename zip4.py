a=[1,2,3,4]
s=[4,5,6,7]
d=[8,9,10,8] 
count=[]
for i,j,k in zip(a,s,d):
    count=count+[i]+[j]+[k]
print(count)    