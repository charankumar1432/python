class Emp:
    company='tcs'
    ceo='elon mask'
    def insert_number(self,name,age,sal,eid):
        self.name=name
        self.age=age
        self.sal=sal
        self.eid=eid
bhanu=Emp()
babu=Emp()
dhoni=Emp()

Emp.insert_number(bhanu,'Bhanu prasad',24,50000,135)
Emp.insert_number(babu,'babu anna',30,80000,432)
dhoni.insert_number('Dhoni sir',49,400000,94793)

