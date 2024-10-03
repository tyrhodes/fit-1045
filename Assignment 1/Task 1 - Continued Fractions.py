"""
* Purpose: This file is designed to allow a non-negative integer n to be used in
           the computation of the appromixation for the value e.
* Organization/Team: Monash University
* Author: Tyler Rhodes (29206804)
* Last Modified: 7 September 2018
"""

# Computation for an approximation for the value of e
# Input: Non-negative integer
n = int(input("Please enter a non-negative integer: "))

# Approximation of e
e = n+1

# This segment calculates the value of e and n as long as the input is greater than 1
while n >= 1:
    e = n+n/e
    n = n-1

# This prints the approximation for the value e
print("An approximation for the value e would be " + str(2+1/e))

