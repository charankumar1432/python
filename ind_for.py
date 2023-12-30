def ind(a):
    count=[] 
    i=0
    for i in range(0,len(a)):
        if a[i] in "aeiouAEIOU":
            count=count+[i]
        i=i+1
    return(count)
b=ind('happy new year')
print(b)        
