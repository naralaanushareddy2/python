            # ------An online shopping website calculates delivery charges--------

def fn():
        # ----------Reads the bill amt from user------------
    amt=int(input("Enter bill value"))
        # ---------Order amount ≥ ₹2000 → Free delivery----------
    if amt>=2000:
        print("you are eligible for free delivery")
        print(amt)
        #   ---------------Order amount ≥ ₹1000 → ₹50 delivery charge----------------
    elif amt>=1000:
        print("₹50 are charged for delivery")
        print(amt+50)
        # ------------------Otherwise → ₹100 delivery charge----------------
    else:
        print("₹100 delivery charge ")
        print(amt+100)
fn()