def s1(a):
    for i in a:
        if type(i) in[list,str,tuple,set,dict]:
            yield len(i)
        else:
            yield i
out=s1([1,[1,2,3],{7,8},'ert',{'a':4},4,2.5])
print(list(out))                