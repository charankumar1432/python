b=('user1@25pass15')
i=0
store=''
while i<len(b):
    if '0'<=b[i]<='9':
        store=store+b[i]
    i=i+1
print(store)        