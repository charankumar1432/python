m=(input('Enter the toggle:-'))
i=0
out=''
while i<len(m):
      if m[i]=='1':
            out=out +'0'
      else:
            out=out+'1'
      i+=1
print(out)                