a='abcd'
out=''
for i ,j in enumerate(a):
   print(j,i,sep='',end='\n')   
   out=out+j+str(i)
print(out)