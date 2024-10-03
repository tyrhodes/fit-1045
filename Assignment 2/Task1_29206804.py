"""
* Purpose: This file is designed to allow a non-negative integer n to be used in
           the computation of n + 1 rows of Pascal's triangle.
* Organization/Team: Monash University
* Author: Tyler Rhodes (29206804)
* Last Modified: 12 October 2018
"""

# Computation for n + 1 rows of Pascal's triangle
# This function prints out the required pascal triangle given the input
def printPascal(n):
    pascal = [1]
    for x in range(n+1):
        # This prints the pascal triangle formatted
        print(*pascal, sep = ' ')
        newline=[]
        newline.append(pascal[0])
        for i in range(len(pascal)-1):
            newline.append(pascal[i]+pascal[i+1])
        newline.append(pascal[-1])
        pascal=newline
    return

# Input: Non-negative integer
n = int(input("Number n: "))

# This calls the function printPascal
printPascal(n)




    
    
