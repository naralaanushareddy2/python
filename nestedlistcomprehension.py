#print sqroot of a number from 1 to 10
l=[i**2 for i in range(1,11)]
print(l)


#print even number from 1 to 11
l=[i for i in range(1,11) if i%2==0]
print(l)

#print odd numbers from 1 to 11
l=[i for i in range(1,11) if i%2 ==1]
print(l)


#nested loop list comprehension 
r=[(i,j) for i in range(1,6) for j in range(6,9) if(i+j)%2==0]
print(r)


#another example
r=[(i,j) for i in range(1,6) for j in range(2,6) if j%i==0]
print(r)

#we can unpack this and prints in separate line
print(*r,sep='\n')



    # ----------------------GENERATORS-------------------------
#using  yield
def f1():
    for i in range(10):
        yield(i)
r=f1()
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__()) #how many times u write next() only that many times you will print the output


#using for loop
def f2():
    for i in range(10):
        yield i
r=f2()
for v in r:
    print(v)  #using for loop we can print all the values at once
 