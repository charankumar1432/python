class Grand:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Parent(Grand):
    def __init__(self,c,d):
        self.c=c
        self.d=d
class Child(Parent):
         pass
obj=Grand(11,22,33,44)