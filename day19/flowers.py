print("flowers are beautiful")
def rose():
    print("Rose is in red")
def lotus():
    print("lotus is in pink")
flower=input("enter the flower name rose/lotus :").strip().lower()
if flower=='rose':
    rose()
elif flower=='lotus':
    lotus()
else:
    print("enter the flower name properly")
