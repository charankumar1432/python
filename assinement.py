arr=[0,1,-3,2,-1]
sum=int(input('Enter teh values:'))
for i in range(len(arr)):
        for i in range(len(arr)):
              if j>i:
                  for k in range(len(arr)):
                     if k>j:
                        if arr[i]+arr[j]+arr[k]==sum:
                            print({arr[i],arr[j],arr[k]})
              
