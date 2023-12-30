def l(var,i=0):
    if len(var)-1==i:
        return var[i]
    return var[i]+l(var,i+1)
a=[1,2,3,4,5,6]
out=l(a)
print(out)