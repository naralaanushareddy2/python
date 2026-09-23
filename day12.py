#FOR LOOP PROBLEMS
#important problems
#1. print numbers from 1 to 10 in one line
for i in range(1,11):
    print(i,end=' ')
print()

#2. print even numbers from 5 to 30 in one line
for z in range(5,31):
    if z%2==0:
        print(z,end=' ')
print()
#3. print odd numbers from 5 to 30 in one line
for a in range(5,31):
    if a%2==1:
        print(a,end=' ')
print()
#4. print numbers divisible by 5 from 1 to 30 in one line
for i in range(1,31):
    if i%5==0:
        print(i,end=' ')
print()
#5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
for i in range(1,101):
    if i%5==0 and i%7==0:
        print(i,end=' ')
print()
#6. sum of numbers from 10 to 25
for i in range(10,26):
    sum=+i
    print(sum)
print() 

#7. sum of numbers in list [4,3,2,5,6,7] 
sum=0
n=[4,3,2,5,6,7]
for i in n:
    sum += i
print(f'the sum of numbers in {n} is {sum}')
#8. multiplication table of a number 
n=6 
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
print()
#9. factorial 
n=int(input("enter a number to find factorial"))
p=1
for i in range(1,n+1):
    p=p*i
print(p)
#9. fibonacci 
a = 0
b = 1 
n = 10 
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b 
print()

# or in another way try this
n=int(input("enter the number to find the fibonacci"))
n1=0
n2=1
sum=0
print(n1,n2,end=' ')
for i in range(n-2):
    sum=n1+n2
    n1=n2
    n2=sum
    print(sum,end=' ')
print()
#10. reverse a string
        # 012345
# string = 'rakesh'
# rev = ''
# for i in range(len(string)-1, -1, -1):
#     rev = rev + string[i]
# print(f'Revers of {string} is {rev}')


# another method
n=input("enter a string to make it reverse")
for i in n[::-1]:
    print(i,end=' ')
print()
#11. count vowels in a string
v='a','e','i','o','u','A','E','I','O','U'
count=0
n=input("enter a string to count vowels")
for i in n:
    if i in v:
        count+=1
print(count)
print()
#12. count z's and y's in a string
n=input("count z's and y's in a string")
count=0
for i in n:
    if i=='z' or i=='y' in i:
        count+=1
print(count)
print()
#13. check whether a number is prime number or not 
n=int(input("enter a number to check it is prime or not"))
flag=False
for i in range(2,n-2):
    if n%i==0:
        flag=True
        break
if flag:
    print("not a prime number")
else:
    print("prime number")
        

print()
print()

#WHILE LOOP PROBLEMS
#print 1 to 10 with while loop
i=1
while i<=10:
    print(i)
    i+=1
print()
#print even numbers from 1 to 10
i=1
while i<=10:
    if i%2==0:
        print(i)
    i+=1
       
#print numbers divisible by both 5 and 7 from 1 to 500 
i=1
while i<=500:
    if i%5==0 and i%7==0:
        print(i)
    i+=1
# count digits
n=int(input())
i=0
while n>0:
    n=n//10
    i+=1
print(i)
    
#reverse a number
n=int(input())
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
    
    
#palindrome number
n=int(input())
original=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if original==rev:
    print("its a palindrome") 
else:
    print("not a palindrome")
#palindrome string without slicing, without built in function
# Armstrong number
n = int(input("enter a number to find it is armstrong number or not"))
original = n
count = 0
total = 0
# Count the number of digits
while n > 0:
    n = n // 10
    count += 1
# Restore the original number
n = original
# Calculate Armstrong value
while n > 0:
    digit = n % 10
    total = total + digit ** count
    n = n // 10
# Check
if total == original:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
    
   
    
