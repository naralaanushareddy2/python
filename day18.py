#List Comprehension
#for
a = []
for x in range(1, 11):
    a.append(x)
print(a)    #1 2 3 4 5 6 7 8 9 10
#create same list with comprehension

#for-if
a = []
for x in range(1,11):
    if x % 2 == 0:
        a.append(x)  
print(a) #[2 4 6 8 10] 
#create same list with comprehension

#for-if-for-if 
a = []
for x in range(1,5):
    if x % 2 == 0:
        for y in range(1,4):
            if x + y == 5:
                a.append((x,y))
print(a)        #[(2,3),(4,1)]
#create same list with comprehension

# #set comprehension
l = [3,4,3,5,6,7,6]
#create list, set, dict comrehension with above list

#function
def numbers():
    return 1 
    return 2 
n = numbers()
print(n)       #1
print(type(n))  #class 'int'

#generators
def numbers():
    yield 1 
    yield 2 
    yield 3 
    yield 4 
n = numbers() 
print(n)
print(type(n))  #class 'generator'
print(next(n))     #1
print(next(n))  #2
print(n.__next__()) #3
print(n.__next__()) #4
# print(next(n))  #throws error

def evennumbers():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x 
n = evennumbers()
print(next(n))      #2 4 6 8
print(n.__next__())
for x in n:
    print(x)

# #write generator to generate odd numbers
def oddnumbers():
    for i in range(1,10):
        if i%2==1:
            yield i
n=oddnumbers()
print(next(n))
for x in n:
    print(x)
print()
            
# #write generator to generate even numbers
def evennum():
    for i in range(1,11):
        if i%2==0:
            yield i
n=evennum()
print(next(n))
for x in n:
    print(x)
print()
# #write generator to generate prime numbers
def prime():
    is_prime=False
    for i in range(2,10):
        for j in range(1,11):
            if i%j==0:
                is_prime=True
                yield i
j=prime()
for x in j:
    print(x)