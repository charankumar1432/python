a=[1,9,23,11,65,43]
out=a[0]
out2=a[0]
for var in a:
    if out<var:
         out=var
    for var in a:
        if out2<var and var!=out:
         out2=var
print(out2)    
