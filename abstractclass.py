from abc import ABC,abstractmethod

class car(ABC):
    def __init__(self,name,coler,price):
        self.name=name
        self.coler=coler
        self.price=price
        self.speed=0
    @abstractmethod
    def stop():
        pass
    @abstractmethod
    def speed_up(self):
        pass
    @abstractmethod
    def speed_down():
        pass
class bmw(car):
    def speed_up(self):
        self.spee+=5
    def speed_down(self):
        self.speed-=5
    def stop(self):
        self.speed=0
bmw=bmw('s7','black',500000)
