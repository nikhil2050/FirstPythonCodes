
# Take input as Int 
a = int(input("Enter value : "))


# IF ELSE
if a==0:
    print("Eq 0")
elif a<5:
    print("Lt 5")
else:
    print("Gt 4")


# _ is previous value
tax = 12.5/10
price = 100
price*tax
price +_


# type(x) : DataType of variable
# id(x)   : Return address of variable
# dir(x)  : List all names  and methods of variable 
x = 5
type(x)
id(x)

x = "Some text"
type(x)
id(x)
dir(x)

a1 = a2 = a3 = "All same address for this string"
print(id(a1))
print(id(a2))
print(id(a3))


# None datatype
drink = "Available"
food = None

def menu(x):
    if(x == drink):
        print("In if :",drink)
    else:
        print("In else :",food)
menu(drink)
menu(food)


# is, is not, in, not in
b1 = True
b1 = "True1"
b2 = "True1"
if b1 is True:
    print("Yeah")
elif b1 is "True1":
    print("Yeah 2")
else:
    print("Naah")

# Import
from math import floor
#help("math.ceil")
floor(3.4)
ceil(3.4)
pi
sin(12)

c1,c2,c3 = 10, 10.67, 45.j
print(c1,"",c2,"",c3)
print(type(c1),"",type(c2),"",type(c3))


# List
mylist1 = [10, 10.67, 45.j, 10]
mylist1.append("a")
mylist1
mylist1.count(10)  # Count 10 in list
type(mylist1)
#dir(mylist1)


# Tuple
mytuple1 = (10, 10.67, 45.j, 10)
#type(mytuple1)
#dir(mytuple1)


# Dictionary
mydict1 = {}
mydict1["one"]="onee"
mydict1["one"]="onee1"
mydict1["two"]="twoo"

#dir(mydict1)

mydict2 = {1:"onee", 2:"twoo", "3":"threeee"}
type(mydict2)


#Set
myset = {'a',1,'b','a'}
myset


# Conversion type
e1 = float("2.55")
e2 = str(25)
set(['a',1,'b','a'])
set({'a',1,'b','a'})
tuple(['a',1,'b','a'])
tuple({'a',1,'b','a'})
tuple(('a',1,'b','a'))
list("hello")
#dict([(1,542),(2,523),(3,34)])    #Not working


# Print with formats
print(1,2,3,4)
print(1,2,3,4,sep='*')
print(1,2,3,4,sep='#', end='&\n')
f1,f2 = 123, 456
print('The value of x is {} and y is {}'.format(f1,f2))
print('The value of x is {f1} and y is {f2}'.format(f1 = 1234, f2 = 5678))


print(list(range(101,200,2)))


## Enumerate list with FOR-loop
list2 = [12,34,56]
for i in list2:
    print(i)
else:
    print("Empty\n")

for i,j in enumerate(list2):
    print(i," ",j )    


## WHILE-loop
num =1
while num < 200 :
    print(num)
    num= num*2

