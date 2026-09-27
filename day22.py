#terminates the program, no alternate action
print('1')  #1
print('2')  #2
# a = 4 / 0  
print('3')  #3
print('4')  #4

# performs alternate action and continues the program
print('1')    #1
print('2')   #2
try:
    a = 4 / 0 
except ZeroDivisionError:
    print("message: Zero Division Error has occured")   #message: Zero Division Error has occured
print('3')    #3
print('4')  #4

# try:
    # print('Examples of syntax errors')
    # a = (1,2,3))     #unmatched paranthesis
    # s = "rakesh""    #unmatched quotes
    # 5 = x            #invalid assignment
    # l = [1 2 3]      #missing comma 
    # if = 21          #using keywords
    # a = 10 
        # b = 20       #incorrect indentation
    # if 10            #missing colon
        # print(True)
# except:
    # print('except suite')



# a = 10 / 0
try:
    print("Examples of runtime errors")
    x = 10 / 0 
    # print(y)   #y is not defined so we can't access                
    a = [1, 2, 3]; print(a[5])   
    d = {"a": 1}; print(d["b"])                    
    int("abc")                   
    "a" + 10                    
    # import abcdef                #module not found error
except IndexError:
    print(1)
except IndexError:
    print(2)
except KeyError as ke:
    print(3, ke)
except (ValueError, TypeError):
    print(4)
# except (ValueError as ve, TypeError as te):
#     pass 
except (ValueError, TypeError) as e:
    pass
except ZeroDivisionError:
    print(5)
#catch-all
except Exception as e:
    print(6)
except:
    print(7)
# except as e:
#     pass



# else and finally
try:
    a = 10 / 4 
except IndexError:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)    #3
finally:
    print(4)    #4

try:
    a = 10 / 0
except IndexError:
    print(1)
except ZeroDivisionError:
    print(2)    #2
else:
    print(3)
finally:
    print(4)    #4
    
try:
    a = 10 / 0 
except IndexError:
    print(1)
except ModuleNotFoundError:
    print(2)
finally:
    print(3)    #3

#Handle child error before parent error
try:
    10 % 0 
except ArithmeticError:
    print('Arithmetic Error')   #Arithmetic Error
except ZeroDivisionError:
    print('Zero Division Error')
# reorder
try:
    10 % 0 
except ZeroDivisionError:
    print('ZeroDivisionError')  #ZeroDivisionError
except ArithmeticError:
    print('ArithmeticError')


#User defined excecption and raise 
#simple UDE
class StudentAlreadyExists(Exception):
    pass 
raise StudentAlreadyExists('Student with rollno 23 already exists')   #raise StudentAlreadyExists('Student with rollno 23 already exists')
raise StudentAlreadyExists('Student with rollno 22 already exists')

#Parameterized UDE
class StudentNotFound(Exception):
    def __init__(self, rollno, name):
        self.rollno = rollno 
        self.name = name 
        #if this is not there, when object is printed prints tuple of all passed values
        super().__init__(f'Student rollno: {rollno} with name {name} is not found')
raise StudentNotFound(1, 'rakesh')
raise StudentNotFound(2, 'adhithya')
try:
    raise StudentNotFound(1, 'rakesh')
except StudentNotFound as snf:
    print(snf)          
    print(snf.rollno)   #individual variables
    print(snf.name)     #individual variables 


# final tricky to understand exceptions:
try:
   stmt1
   stmt2
   stmt3
except XError:
   stmt4 
except YError:
   stmt5 
else:
   stmt6
finally:
   stmt7
stmt8 
# questions:
# 1. when no error.     #prints finnaly block
# 2. when stmt2 throws XError.  
# 3. when stmt2 throws ZError. 
# 4. when stmt2 raise XError, stmt4 raise YError. 
# 5. when stmt2 raise XError, stmt7 raies YError. 
