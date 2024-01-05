class module:
    def __init__(self,a):
        self.a=a
    def __mul__(self,other):
        return self.a*other.a
x=module()
y=module()