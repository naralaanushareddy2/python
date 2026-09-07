
                # ------HACKER RANK Questions------------


#!/bin/python3
# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if (n%2==1):
        print("Weird")
    if (n%2==0):
        if (n>=2 and n<=5):
            print("Not Weird")
        elif (n>=6 and n<=20):
            print("Weird")
        else:
            print("Not Weird")
            
            

# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# Input Format

# Read , the year to test.

# Constraints


# Output Format

# The function must return a Boolean value (True/False). Output is handled by the provided code stub.

# Sample Input 0

# 1990
# Sample Output 0

# False
# Explanation 0

# 1990 is not a multiple of 4 hence it's not a leap year.


def is_leap(year):
    
    
    # Write your logic here
    
    if (year%400==0):
        return True
    elif (year%100==0):
        return False 
    if (year%4==0):
        return True
    else:
        return False

year = int(input())
print(is_leap(year))
