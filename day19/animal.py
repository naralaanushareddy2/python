print("All Animals can't roar")
def lion():
        print("Lion will Roar")
def cat():
        print("meow meow")
animal=input("enter animal name :").strip().lower()
if animal=="lion":
    lion()
elif animal=="cat":
    cat()
else:
    print("i don't how the animal will make sounds")
    