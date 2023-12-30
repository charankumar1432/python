a=("Enter the value")
count=0
for i in range(1,a):
    if a%i==0:
        count=count+i
if count==a:
    print('perfect')
else:
    print('not perfect')                