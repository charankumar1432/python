class Base:
    a=10
    b=20
    def __init__(self,c):
        self.c=c
    def display(self):
        print(self.c)
class derived(Base):
    def __init__(self,c,e,d):
        Base.__init__(self,c)
        self.e = e
        self.d = d
    def display(self):
        super().display()
        print(self.e,self.d)
obj =derived(56,58,60)