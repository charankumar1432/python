class Base:
    a=10
    b=20
    def __init__(self,c):
        self.c=c
class derived(Base):
    def __init__(self,c,e,d):
        Base.__init__(self,c)
        self.e = e
        self.d = d
obj =derived(56,58,60)