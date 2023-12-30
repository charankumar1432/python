seats=int(input('enter the number:'))
option=int(input('enter the value:'))
match option:
    case 1:
        print('dimond class')
        amt=seats*200
    case 2:
        print('gold')
        amt=seats*150
    case 3:
        print('silver')
        amt=seats*100
    case _:
        print('invalid option')
        amt=None 
print(amt)        
