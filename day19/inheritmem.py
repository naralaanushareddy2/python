

from animal import lion,cat
animal = input("Enter animal name: ").strip().lower()
if animal=="lion":
    lion()
elif animal=="cat":
    cat()
else:
    print("i don't how the animal will make sounds")
    