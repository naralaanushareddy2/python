#single import
import calculator 

# #members are not imported
# #functions
# print(add(20,10))       #we imported module not the mem if u want to access the mem you need to mention the module.mem() then you can access the mem of the module but can't access directly the mem without name
# print(sub(20,10))
# print(mul(20,10))
# print(div(20,10))
# #classes
# c = Calculator()
# #objects 
# print(c1)
# print(c2)

#module is imported
#functions
print(calculator.add(20,10))
print(calculator.sub(20,10))
print(calculator.mul(20,10))
print(calculator.div(20,10))
#classes
c = calculator.Calculator()
#objects 
print(calculator.c1)
print(calculator.c2)

 