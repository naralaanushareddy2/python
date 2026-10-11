import re

# Match Object Methods
#       012345
text = 'abc123'
match = re.search(r'\d+', text)
print(match)     #returns the matched obj     
print(match.group())     #123
print(match.start())   #3
print(match.end())      #6
print(match.span())       #(3, 6) 
print()


# Match Object group()
text = 'Name: Rakesh, Age: 25'
match = re.search(r'Name: (\w+), Age: (\d+)', text)
print(match.group())    #Name: Rakesh, Age: 25
print(match.group(1))  # Rakesh
print(match.group(2))    # 25
print(match.groups())  # ('Rakesh', '25')
print()


# re.match()
match = re.match(r'abc', 'abcdef')
print(match)        #returns the matched obj     
print(match.group())  #abc
print()

match = re.match(r'abc', 'xyzabc')
print(match)          #None because match will start searching at starting only if not found at starting it will return none
print()


# re.search()
match = re.search(r'abc', 'xyzabc123')
print(match)     #returns the matched obj   
print(match.group())  #abc
print()


# re.fullmatch()
print(re.fullmatch(r'\d+', '12345'))    #returns the matched obj of digits
print(re.fullmatch(r'\d+', '123abc'))  #None because it returns only if the given condition is fully matched else returns None
print()


# re.findall()
print(re.findall(r'\d+', '10 20 30'))   #['10','20' ,'30']            
print(re.findall(r'[A-Z]', 'Python JAVA C++'))  #['P','J','A','V','A','C']
print()


# re.finditer()
text = 'abc123 xyz456'
for match in re.finditer(r'\d+', text):
    print(match)    #reurns the matched obj   and 456 is also matched obj 
    print(match.group())   #123   and 456
    print(match.start())     #3   and 10
    print(match.end())  #6  and 13
    print()


# re.split()
text = 'apple,banana;orange'
print(re.split(r'[,;]', text))  #['apple','banana,'orange']
print()


# re.sub()
text = 'Python is easy. Python is powerful.'
print(re.sub(r'Python', 'Java', text))  
print()


# re.subn()
text = 'cat dog cat cat'
print(re.subn(r'cat', 'lion', text))  #('lion dog lion lion', 3)
print()


# re.compile()
pattern = re.compile(r'\d+')
print(pattern.search('abc123')) #returns the matched obj i.e 123 
print(pattern.findall('10 20 30'))    #['10','20','30']
print()