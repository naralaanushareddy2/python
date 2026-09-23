#multiple members
from calculator import add, sub 
from physics import newtonsfirst, newtonssecond 
from biology import dna 

print(add(20,10))
print(sub(20,10))
# print(calculator.sub(20,10)) 
# print(mul(20,10))


print(newtonsfirst())
print(newtonssecond())
# print(physics.newtonssecond())   #we jst imported member in the module so we can directly access the mem not the module
# print(newtonsthird())


print(dna())
# print(biology.dna())
# print(genes())
