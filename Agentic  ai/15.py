class Car:
    def __init__(self):
        self.brand='Lamborghini Aventador'
        self.cost=8.70
        self.color='Yellow'
def start_engine(self):
    print(self.brand,'Engine started')
def start_gear(self):
    print(self.brand,'shifting gear')
def  accelerate(self):
    print(self.brand,'accelerating')

c1=Car()
print(c1.brand)
print(c1.cost)
print(c1.color)
c1.start_engine()
c1.start_gear()
c1.accelerate()