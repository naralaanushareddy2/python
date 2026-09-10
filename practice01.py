        # -----------Supermarket Discount System--------

def fn():
    # ----------reads the bill amt from user-----------
    amt=int(input("Enter the bill amt")) 
        # ----------If purchase amount is ₹5000 or more → 20% discount
    if amt>=5000:
        print("20% discount")
        print("discount:",(20/100)*amt)
        print("amt to pay :",(80/100)*amt)
        # -----------If purchase amount is ₹3000 or more → 10% discount-------------------
    elif amt>=3000:
        print("10% discount")
        print("discount :",(10/100)*amt)
        print("amt to pay :",(90/100)*amt)
        # ------------If purchase amount is ₹1000 or more → 5% discount-------------------
    elif amt>=1000:
        print("5% discount")
        print("discount :",(5/100)*amt)
        print("amt to pay :",(95/100)*amt)
        # --------Otherwise → No discount----------------
    else:
        print("plz shop above 1000 to get discount")
fn()