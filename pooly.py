class model:
    @staticmethod
    def add(a,b):
        return a+b
    @StopAsyncIteration
    def add(a,b,c):
        return a+b+c
obj=model()
obj.add()