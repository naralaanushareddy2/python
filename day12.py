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
#9. fibonacci 
a = 0
b = 1 
n = 10 
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b 
# print()

#10. reverse a string
        # 012345
# string = 'rakesh'
# rev = ''
# for i in range(len(string)-1, -1, -1):
#     rev = rev + string[i]
# print(f'Revers of {string} is {rev}')
#11. count vowels in a string
#12. count z's and y's in a string
#13. check whether a number is prime number or not 





#WHILE LOOP PROBLEMS
#print 1 to 10 with while loop
#print even numbers from 1 to 10
#print numbers divisible by both 5 and 7 from 1 to 500 
#count digits
#reverse a number
#palindrome number 
#palindrome string without slicing, without built in function
#armstrong number
