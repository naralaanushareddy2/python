# -----------STAR PATTERNS------------------
# *****
# ****
# ***
# **
# *
n=3
for i in range(0,n+1):
    print(i,'*')
print()



# to print if reverse
n=3
for i in range(n,0,-1):
    print(i,'*')
print()


#    *   
#   * *  
# * * *
# to print on a triangle
n=5   
for r in range(n):
    print((n-r)*' ' + r*'* ')
print()
    
# to print in reverse    
n=5  
for r in range(n,0,-1):
    print((n-r)*' ' + r*'* ')
print()
    
# to print sqare border
n=int(input("enter a number to print square"))
for r in range(n):
    for c in range(n):
        if r==0 or r==n-1 or c==0 or c==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
print()


# print a special shape
n = int(input("enter a number to print special shape"))

for r in range(n):
    if r == 0:
        print((2*n-1) * '*')
    else:
        print((n-r) * '*' + (2*n-1) * ' ' + (n-r) * '*')
        
        
        
# print a special shape in reverse
n = int(input("enter a number to print special shape in reverse"))

for r in range(n,-1,-1):
    if r == 0:
        print((2*n-1) * '*')
    else:
        print((n-r) * '*' + (2*n-1) * ' ' + (n-r) * '*')
        
        
# to print star
n=int(input("enter a number to print star"))
for r in range(n):
    for c in range(n):
        if r==c or r==n//2 or c==n//2 or c==n-r-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
print()