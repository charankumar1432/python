a=int(input("Enter the value:"))
i=1
temp=False
while i<=a:
    if a%i==0 and i!=1 and i!=a:
      count=True
    i+=1
if not temp:
    print("not temp")
else:
    print("temp")   