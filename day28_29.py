#Method overriding
class Vehicle:
    def drive(s):
        print('Vehicle is driving')
class Bike(Vehicle):
    def drive(s):
        print('Bike is driving')
v = Vehicle() 
b = Bike() 
v.drive()
b.drive()


#Method overloading 
def display(name, age):
    print('1') 
def display(age, marks):
    print('2') 
def display(age, name, marks):
    print('3') 
display(1, 3, 5)

def display(*a):
    print(a) 
display(2)
display(3,4)
display(3,4,23,5,235,23,5235)

def display(**a):
    print(a) 
display(a=10, b=20, c=30)


def display(a, b=10, c=20, d=30):
    print(a + b + c + d)
display(1)           #61
display(1, 2)        #53
display(1, 2, 3)     #36
display(1, 2, 3, 4)  #10


#Operator overloading 
print(1 + 2) 
print((1,2,3) + (4,5,6))

print(4 * 8)
print('anu' * 3)
print([1,2,3])
print(*[1,2,3])

from abc import ABC, abstractmethod
class Phone(ABC):
    @abstractmethod 
    def brand():
        pass 
    @abstractmethod 
    def model():
        pass 
    def os():
        print('Android')
class Samsung(Phone):
    def brand():
        print('Sumsung')
s = Samsung()