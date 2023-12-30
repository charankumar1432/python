class Sbi:
    branch='palamner'
    manager='jo'
    ifsc='233HJHQSX7'
    def __init__(self,name,age,sal,eid,bal):
        self.name=name
        self.age=age
        self.sal=sal
        self.eid=eid
        self.bal=bal
    def credit(self,amt):
        self.bal+=amt
    def debit(self,amt):
        self.balence-+amm
    @classmethod
    def change_mgr(cls,new):
        cls.manager=new
    @staticmethod
    def add(a,b):
        return a+b
chandra=Sbi('chandu',65,23367,4554,5767)
lokesh=Sbi('lokesh nayadu',45,60000,345623,3000)