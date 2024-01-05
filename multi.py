class add:
    @staticmethod
    def add(a,b):
        return a+b
class sub:
    @staticmethod
    def sub(a,b):
        return a-b
class Child(add,sub):
    pass

