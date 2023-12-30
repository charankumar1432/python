class Emp:
    company='tcs'
    ceo='elon mask'
    def insert_number(obj,name,age,sal,eid):
        obj.name=name
        obj.age=age
        obj.sal=sal
        obj.eid=eid
bhanu=Emp()
babu=Emp()

Emp.insert_number(bhanu,'Bhanu prasad',24,50000,135)
Emp.insert_number(babu,'babu anna',30,80000,432)

print(bhanu.company)
