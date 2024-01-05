import csv
with open('mca.csv','w',newline='')as csvfile:
    data=csv.writer(csvfile)
    data.writerow(['id','name','mobile','mail'])
    data2=[
        [1,'jo',9948366547,'jo@9845j405t45g'],
        [2,'chandu',2545674564,'chan@1234'],
        [3,'kirak',4098456797,'kiran@911070'],   
         ]
    data.writerows(data2)
