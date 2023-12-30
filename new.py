def aa(a):
    if a%2==0:
        return True
    else:
        return False
out=filter(aa,[11,243,344,12,24])
print(list(out))    