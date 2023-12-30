class Grand:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Parent(Grand):
    def __init__(self,c,d):
        self.c=c
        self.d=d
class Child(Parent):
    e=20
    f=40
obj=Child(11,22,32,43)