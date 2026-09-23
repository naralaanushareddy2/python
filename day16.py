# #local, global variable
# a = 1
# def f1():
#     b = 2
#     print(a)   
#     print(b) 
#     print(c)
# def f2():
#     c = 2 
#     print(a)  
#     print(b) 
#     print(c)  
# f1()
# f2()
# print(a)      
# print(b)      
# print(c)     

# #call by value, call by reference
# # call by value 
# def f1(a):
#     a = 100
# a = 4
# f1(a)
# print(a)      

# #call by reference
# def f2(a):
#     a = [10, 20, 30]
# a = [1, 2, 3]
# f2(a)
# print(a)    

# def f3(a):
#     a = [100, 200, 300]
#     a[2] = 200
# a = [1, 2, 3]
# f3(a)
# print(a)    

# recursive functions
# factorial
# n=int(input("enter factorial number"))
# def fac(n):
#     if n==0:
#         return 1
#     return fac(n-1)*n

# print(fac(n))
# fibonacci
n=int(input("enter the number to find the fibonacci"))
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-2)+fib(n-1)
print(fib(n))




