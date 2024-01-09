s=('he@idg#d14')
i=0
out=''
while i<len(s):
       if not ('A'<=s<='Z' or 'a'<=s<='z' or '0'<=s<='9'):
              out=out+''
       else:
            out=out+s[i]
       i+=1
print(out)                   
          
