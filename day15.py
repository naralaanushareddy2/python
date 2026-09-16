def add(a, b):
    print('add function')  # add function
    c = a + b 
    return c 
    print('HI')     #not printed because it is after return
def sub(a, b):
    print('sub function')   #sub function
    c = a - b
    return 
def div(a, b):
    print('div function')   #div function
    c = a / b 
x = add(10, 15)    #25
y = sub(20, 10)   #none becuase the default value for return is none
z = div(25, 10)   #none becuase the default value for return is none even you didn't specified the return keyword
print(x)
print(y)
print(z)
print()

#Type of arguments
def detail(name, age, rollno):
    print(f'My name is {name}')  #My name is rakesh  //My name is 20  
    print(f'My age is {age}')       #My age is 20    //My age is A101
    print(f'My rollno is {rollno}')     #My rollno is A101  //My rollno is rakesh
#positional 
detail('rakesh', 20, 'A101')
detail(20, 'A101', 'rakesh')
#keyword
detail(age=20, rollno='A101', name='rakesh')  #My name is rakesh   #My age is 20 #My rollno is A101
detail(rollno='A101', age=20, name='rakesh')     #My name is rakesh   #My age is 20 #My rollno is A101
#default
def add(a, b=10, c=20):
    return a + b + c 
print(add(1))  #31
print(add(1,2)) #23
print(add(1,2,3)) #6
print(add(c=3, a=1, b=2)) #6

#order of = in function def. DA after NDA
# def sub(a=10, b, c):
    # pass    throws error because != after == we have to specify

#order of = in function call. KA after PA
# add(a=10, b, c)

def f1(*a):
    print(a) #{1,2,3,4}
    print(type(a))  #class 'tuple'
f1(1,2,3,4)   

def f2(**a):
    print(a)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(type(a))  #class dict
# f2(1,2,3,4)  #it doen't takes positional arg
f2(a=1, b=2, c=3, d=4)