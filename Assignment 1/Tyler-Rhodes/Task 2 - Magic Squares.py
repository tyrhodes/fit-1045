"""
* Purpose: This file is designed to check if a document containing a potential
           magic square is a valid one.
* Organization/Team: Monash University
* Author: Tyler Rhodes (29206804)
* Last Modified: 6 September 2018
"""

# A check to see if a magic square is a partial magic square that has certain properties

# This function checks for invalid row, column and diagonal values
def checkMagicSqr(magicSquare, magicSum, userX, userY, n):
    # rows
    for row in magicSquare:
        # print(magicSum, str(sum(row)))
        if sum(row) > magicSum:
            if userX != 0 and userY != 0:
                magicSquare[userY][userX] = 0
            return "Invalid magic square"

    # cols
    # The following nested loops store the elements that need to be removed
    for h in range(0, n):
        colSum = []
        for v in range(0, n):
            colSum.append(magicSquare[v][h])
        if sum(colSum) > magicSum:
            if userX != 0 and userY != 0:
                magicSquare[userY][userX] = 0
            return "Invalid magic square"
        else:
            colSum = []
            continue

    # diags
    # Create two empty lists to store invalid elements
    diag1 = []
    diag2 = []
    for x in range(0, n):
        diag1.append(magicSquare[x][x])
        diag2.append(magicSquare[(n-1)-x][x])
        if sum(diag1) > magicSum:
            if userX != 0 and userY != 0:
                magicSquare[userY][userX] = 0
            return "Invalid magic square"
    return "Magic Square is valid"

# This function inputs a file containing a magic square and then creates a magic square array given valid user input
def main():
    # Input: Name of magic square file
    fileName = input("Please input the name of the file: ")
    magicSquarefile = open(fileName, 'r')

    lines = magicSquarefile.readlines()

    n = len(lines[0].split())
    
    #Use variables to track the magic sum, x and y inputs
    magicSum = 0
    userX = 0
    userY = 0

    for line in lines:
        # Split the lines
        lineElems = line.split() 
        if "Magic" in lineElems:
            magicSum = int(lineElems[-1])
            # This prints the magic sum
            print("Magic sum: " + str(magicSum))
            print("")
    
    ## Create MagicSquare array
    magicSquare = [[0] * n for i in range(n)]
    for k in range(0,n):
        for i in range(0,n):
           # Cast each "cell" as integer and insert to the magic square
           magicSquare[k][i]=int(lines[k].split()[i])

    isValid = checkMagicSqr(magicSquare, magicSum, userX, userY, n)
    if "Invalid" in isValid:
        print(isValid)
        quit()
    else:
        print(isValid)

    # User entry and check magic square properties        
    while True:
        # Print Magic Square
        for k in range(0,n):
            print('\n')
            for i in range(0,n):
               print(str(magicSquare[k][i]) + " ", end="")

        print('\n\n')
        # Input: empty square x value
        userX=int(input("Enter an empty square x value:"))-1
        # Input: empty square y value
        userY=int(input("Enter an empty square y value:"))-1
        if magicSquare[userY][userX] != 0:
            while magicSquare[userY][userX] != 0:
                print("That cell is already taken")
                print(magicSquare[userY][userX])
                # Input: empty square x value
                userX=int(input("Enter an empty square x value:"))-1
                # Input: empty square y value
                userY=int(input("Enter an empty square y value:"))-1
        # Input: integer greater than 0
        userNum=int(input("Input an integer greater than 0: "))

        magicSquare[userY][userX] = userNum

        # This prints the magic square, magic sum, x, y and number
        print(checkMagicSqr(magicSquare, magicSum, userX, userY, n))

main()
