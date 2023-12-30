s="abc@123$321lojp"
out=0
for var in s:
    if '0'<=var<='9':
        out=out+int(var)
print(out)        
