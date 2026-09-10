    # ---------- Electricity Bill Calculation-----------
def fn():
        # -----An electricity company calculates the bill based on the number of units ----------
    unit=int(input("Enter Number of Units used"))
    # ------------Units Consumed 
    # ----------Rate per Unit    0–100.    ₹2---------
    if unit>0 and unit<=100:
        print("Bill :",unit*2)
        # ----------101–200.  ₹3--------------
    elif unit>=101 and unit<=200:
        print("Bill :",unit*3)
        # ----------201–300    ₹5---------------
    elif unit>=201 and unit<=300:
        print("Bill :",unit*5)
        # -----------Above 300.   ₹7-----------
    else:
        print("Bill :",unit*7)
fn()