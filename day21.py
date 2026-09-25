import getpass
balance=0
p1=int(getpass.getpass("Set the pin :  "))
if len(str(p1))!=4:
    print("password must be exactly 4 digits")
    exit()
p2=int(getpass.getpass("Reenter the pin :  "))
if p1!=p2:
    print("password is not matching ")
    exit()
pin=p2
while True:
    print('---------------------------------')
    print("1. Balance Enquire")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    n=int(input("Enter your choice : "))
    match n:
        case 1:
            p=int(getpass.getpass('plz enter the pin'))
            if p!=pin:
                print("pin is incorrect")
                continue
            print(f'balance amt is {balance}')
            continue
        case 2:
            p=int(getpass.getpass('plz enter the pin'))
            if p!=pin:
                print("pin is incorrect")
                continue
            amt=int(input("enter the amt to deposit"))
            balance+=amt
            print(f'amt deposited successfully. the balance is {balance}')
            continue
        case 3:
            p=int(getpass.getpass('plz enter the pin'))
            if p!=pin:
                print("pin is incorrect")
                continue
            amt=int(input("enter the amt to withdraw"))
            if amt>balance:
                print("insufficient balance")
                continue
            balance-=amt
            print(f'amt is withdrawn succesfully. the balance amt is {balance}')
            continue
        case 4:
            exit()
            
    