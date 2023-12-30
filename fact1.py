def fact(a,i=1):
    if a==i:
        return i
    return i * fact(a,i+1)
out=fact(10)
print(out)