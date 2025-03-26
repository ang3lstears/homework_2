print('number 3')
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def __getattr__(self, item):
        return "This attribute is not available"
c = Car("Toyota", "Corolla")
print(c.make)
print(c.color)


print('number 4')
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __setattr__(self, name, value):
        if name in ("width", "height"):
            super().__setattr__(name, value)
        else:
            raise AttributeError("Local attributes are not allowed")
r = Rectangle(10, 20)
r.width = 15
r.height = 25
print(r.width)
print(r.height)
r.color = 'red'