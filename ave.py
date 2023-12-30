def b(a):
    for i in a:
        if len(i)%2==0:
            yield (i[0]+i[-1])/2
        else:
            yield i[len(i)//2]
out=b[(1,2),[3,4,5,6],(4,3,2),[9,3,6],(11,12,13)]
print(list(out))                