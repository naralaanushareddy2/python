#find the greatest number
l=input("enter number to find the greatest number").split()
largest=l[0]
for i in l:
    if i>largest:
        largest=i
print(largest)


# //smallest number
n=input("enter numbers to find the smallest number ").split()
smallest=n[0]
for i in n:
    if i<smallest:
        smallest=i
print(smallest)

# //using conditions
a=10
b=5
c=56
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)


# //gcd of a numbers
l=list(map(int,input("enter the numbers to find gcd :").split()))
smallest=l[0]
for i in l:
    smallest=i
a=l[0]
b=l[1]
for n in range(i,0,-1):
    if a%n==0 and b%n==0:
        print("GCD :",n)
        break