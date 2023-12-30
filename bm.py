print('Welcome to book my show')
name=input('Enter your name:_')
seats=int(input('Enter no of seats:-'))
categary=int(input('please select 1 ---->dimond class \n 2---->gold calss \n 3---->3 silver class'))
if categary==1:
    amount=seats*200
elif categary==2:
    amount=seats*150
elif categary==3:
    amount=seats*100
print(f"hi {name} you have booked {seats} seats and total amount is {amount}")