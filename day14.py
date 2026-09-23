# #               ---------NUMBER PATTERN-------------
# # 1 
# # 1 2 
# # 1 2 3 
# # 1 2 3 4 
# # 1 2 3 4 5 
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# # 1 
# # 2 1 
# # 3 2 1 
# # 4 3 2 1 
# # 5 4 3 2 1
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()

# # 1 
# # 2 2 
# # 3 3 3 
# # 4 4 4 4 
# # 5 5 5 5 5     
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=' ')
#     print()
    
# # 1 
# # 1 1 
# # 1 1 1 
# # 1 1 1 1 
# # 1 1 1 1 1     
# for i in range(n+1):
#     for j in range(i):
#         print(1,end=' ')
#     print()
    
# # 1 
# # 2 3 
# # 4 5 6 
# # 7 8 9 10 
# c=1
# for i in range(n):
#     for j in range(i):
#         print(c,end=' ')
#         c+=1
#     print()



# #           -----------ALPHABET PATTERNS-----------
# # A 
# # A B 
# # A B C 
# # A B C D 
# # A B C D E 
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(j+64),end=' ')
#     print()
# # A 
# # B A 
# # C B A 
# # D C B A 
# # E D C B A 
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(chr(j+64),end=' ')
#     print()
# #  A 
# # B B 
# # C C C 
# # D D D D 
# # E E E E E    
# for i in range(n+1):
#     for j in range(i):
#         print(chr(i+64),end=' ')
#     print()
# # A 
# # A A 
# # A A A 
# # A A A A 
# # A A A A A     
# for i in range(1,n+1):
#     for j in range(i):
#         print('A',end=' ')
#     print()
    
# # A
# # B C
# # D E F
# # G H I J 
# c=1
# for i in range(n):
#     for j in range(i):
#         print(chr(c+64),end=' ')
#         c+=1
#     print()
    

#pascal triangle
n=10
for i in range(n):
    num=1
    for j in range(i+1):
        print(num,end=' ')
        num=num*(i-j)//(j+1)
    print()