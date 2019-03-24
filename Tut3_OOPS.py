"""One of the popular approach to solve a programming problem is by creating objects. 
This is known as Object-Oriented Programming (OOP).

An object has two characteristics:
1. attributes
2. behavior

Let's take an example:
Parrot is an object:
    + name, age, color are attributes
    + singing, dancing are behavior

The concept of OOP in Python focuses on creating reusable code. 
This concept is also known as DRY (Don't Repeat Yourself)."""

"""
Inheritance : Process of using details from a new class without modifying existing class.
Encapsulation : Hiding private details of a class from other objects
Polymorphism : Comcept of using common operation in diff. ways from diff. data input
"""

# Class/Static & Instance Variable 
"""
Class/Static Attribute(s) :
    1. It is at class level
    2. It can be access using Class name or self object within Class. Good practice is to use Class name.
    3. It is like class level static variable in Java
    4. The Python approach is simple, it doesn’t require a static keyword.
Instance Attribute(s)
    1. It is available per instance of class i.e. Object """

class ShippingContainer:
    next_serial = 1000     # Class/Static Variable
    
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code   # Instance variable
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        self.next_serial = 10000+ShippingContainer.next_serial
        ShippingContainer.next_serial+=1

obj = ShippingContainer("ESC","noodles")
print(obj.owner_code)        
print(obj.contents)        
print("obj.next_serial",obj.next_serial)        
print("ShippingContainer.next_serial",ShippingContainer.next_serial)        

obj2 = ShippingContainer("ESC2","noodles2")
print(obj2.owner_code)        
print(obj2.contents)        
print("obj2.next_serial",obj2.next_serial)        
print("ShippingContainer.next_serial",ShippingContainer.next_serial)        


# DATA-ENCAPSULATION 
""" Private attributes : Using _ or __ as prefix """
class Computer:
    def __init__(self):
        self.__maxprice = 900
    
    def setMaxPrice(self, p):
        self.__maxprice = p
 
    def getMaxPrice(self):
        return self.__maxprice
 
c = Computer()
#print(c._maxprice)   # AttributeError: 'Computer' object has no attribute '_maxprice'
print("Before: ",c.getMaxPrice())
c.setMaxPrice(12)
print("After: ",c.getMaxPrice())



# POLYMORPHISM

class Parrot:
    def fly(self):
        print("Parrot fly")
    def swim(self):
        print("Parrot swim")
class Penguin:
    def fly(self):
        print("Penguin NO fly")
    def swim(self):
        print("Penguin swim")
def fly_test(bird):
    bird.fly()
prt = Parrot()
png = Penguin()

fly_test(prt)
fly_test(png)



# DELETE Attributes & objects
class ComplexNo:
    def __init__(self, real, img):
        self.real = real
        self.img = img
c1 = ComplexNo(12,34)
print(c1.real)
del c1.real
#print(c1.real)  # AttributeError: 'ComplexNo' object has no attribute 'real
print(c1)
del c1
#print(c1)        # NameError: name 'c1' is not defined


# INHERITANCE
class Bird():
    def __init__(self):
        print("Bird Constr")
    def swim(self):
        print("Swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()          # Call super Constructor
        print("Penguin Constr")
    def run(self):
        print("Run faster")
png = Penguin()
png.swim()
png.run()


# METHOD OVERRIDING
"""
Generally when overriding a base method, we tend to extend the definition rather than simply replace it.
The same is being done by calling the method in base class from the one in 
derived class (calling BaseClass.__init__() from __init__() in DerivedClass).
""""""
Better option is to use the built-in func super().
So, super.__init(3) is equivalent to BaseClass.__init__(self,3)
""""""
2 built-in functions are used to check inheritances:
    1. isinstance() 
    2. issubclass() 
"""
print(isinstance(png, Penguin))  # True
print(isinstance(png, Bird))     # True
print(isinstance(png, object))   # True
print(isinstance(png, int))      # False
print()
print(issubclass(Penguin, Bird)) # True
print(issubclass(bool, int))     # True



# MULTIPLE INHERITANCE & METHOD RESOLUTION ORDER(MRO)
"""When a class extends more than 1 class, it is called Multiple Inheritance
""""""
MultiDerived extends Base1, Base2
"""
class Base1: pass
class Base2: pass
class Base3: pass

class MultiDerived1(Base1, Base2): pass
class MultiDerived2(Base2, Base3): pass

class MultiDerived3(MultiDerived2, MultiDerived1, Base3): pass

print(MultiDerived3.mro())
""" OUTPUT : 
"""""" [<class '__main__.MultiDerived3'>, 
<class '__main__.MultiDerived2'>,<class '__main__.MultiDerived1'>, 
<class '__main__.Base1'>, <class '__main__.Base2'>, 
<class '__main__.Base3'>, <class 'object'>]
"""


# Python uses C3 algo internally to calculate MRO
class A:
    def func(self):
        return "A.func"
class B(A):
    def func(self):
        return "B.func"
class C(A):
    def func(self):
        return "C.func"
class D(B,C):
    pass

D.mro()     # [__main__.D, __main__.B, __main__.C, __main__.A, object]

d = D()
print(d.func()) # B.func



print([1 for i in range(5)])  # [1, 1, 1, 1, 1]
