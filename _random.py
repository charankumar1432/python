import random
num=random.randint(100,800)
while True:
    a=int(input('ent a num:-'))
    if a == num:
        print('congrargulation')
        break
    elif a<num:
        print('enter grate value')
    elif a>num:
        print('enter less num')
