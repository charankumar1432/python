def sum(sv,ev):
    if sv==ev:
        return sv
    return sv + sum(sv+1,ev)
out=sum(1,10)
print(out)
