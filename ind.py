def ind(a):
    count=[] 
    i=0
    while  i<len(a):
        if a[i] in "aeiouAEIOU":
            count=count+[i]
        i=i+1
    return(count)
b=ind('happy new year')
print(b)        
