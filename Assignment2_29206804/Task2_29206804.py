"""
* Purpose: This file is designed to create a list of records of CDs and then
           allow for the sorting and searching of different attributes in the list
* Organization/Team: Monash University
* Author: Tyler Rhodes (29206804)
* Last Modified: 12 October 2018
"""

# A program that creates a list of records about CDs and allows the sorting and searching of different attributes in the list
# Use variables to set dataheaders and dashes for formatted list
dataHeaders = ['TITLE', 'ARTIST', 'GENRE', 'PRICE $']
dash = '-' * 80

# This function creates the database by reading from the filename inputted                     
def CreateDatabase(CD):
    dataFile = open(CD, 'r') 
    aList = dataFile.readlines()
    for n in range(len(aList)):
        aList[n] = aList[n].split(",")
    return aList

# This function prints the list of CDs in a format that is readable for users
def PrintList(aList):
    # This prints dashes
    print(dash)
    # This prints the dataheaders formatted
    print('{:<35s}{:<20s}{:^10s}{:>10s}'.format(dataHeaders[0],dataHeaders[1],dataHeaders[2],dataHeaders[3]))
    # This prints dashes
    print(dash)

    for record in aList:
        title = str(record[0])   
        artist = str(record[1])
        genre = str(record[2])
        price = float(record[3])
        # This prints the data under each dataheader formatted
        print('{:<35s}{:<20s}{:^10s}{:>10.2f}'.format(title,artist,genre,price))
    return

# This function prints all elements in the list of CDs that have the selected index given in the target
def FindBy(search, elem):
    # This prints dashes
    print(dash)
    # This prints the dataheaders formatted
    print('{:<35s}{:<20s}{:^10s}{:>10s}'.format(dataHeaders[0],dataHeaders[1],dataHeaders[2],dataHeaders[3]))
    # This prints dashes
    print(dash)
    
    for record in aList:
        title = str(record[0])   
        artist = str(record[1])
        genre = str(record[2])
        price = float(record[3])

        if elem < 3 and record[elem] == search:
            # This prints the data under each dataheader formatted
            print('{:<35s}{:<20s}{:^10s}{:>10.2f}'.format(title,artist,genre,price))
        elif elem == 3 and float(record[elem]) <= float(search):
            # This prints the data under each dataheader formatted
            print('{:<35s}{:<20s}{:^10s}{:>10.2f}'.format(title,artist,genre,price))
    return

# This function sorts the list of CDs by the given attribute    
def DataSort(aList, elem):
    for recIndex in range(1,len(aList)):
 
        currentRecord = aList[recIndex]
        position = recIndex

        if elem == 3:
            # Check sort property
            while position>0 and float(aList[position-1][elem]) > float(currentRecord[elem]):

                aList[position]=aList[position-1]
                position = position-1

                aList[position]=currentRecord
        else:
            # Check sort property
            while position>0 and aList[position-1][elem]>currentRecord[elem]:

                aList[position]=aList[position-1]
                position = position-1

                aList[position]=currentRecord

# This function displays a menu with given options that have functions
def DisplayMenu():
    while True:
        # This prints the menu for an option to be selected from
        print("""
        1. Print List of CDs
        2. Sort CDs by Title
        3. Sort CDs by Artist
        4. Sort CDs by Genre
        5. Sort CDs by Price
        6. Find All CDs by Title
        7. Find All CDs by Artist
        8. Find All CDs by Genre
        9. Find All CDs with Price at Most X
        10. Quit
        """)

        # Input: Menu option
        option = input("Please enter a menu option: ")

        if option == "1":
            # This calls the function printList
            PrintList(aList)
        elif option == "2":
            # This calls the function DataSort using the first index
            DataSort(aList, 0)
        elif option == "3":
            # This calls the function DataSort using the second index
            DataSort(aList, 1)
        elif option == "4":
            # This calls the function DataSort using the third index
            DataSort(aList, 2)
        elif option == "5":
            # This calls the function DataSort using the fourth index
            DataSort(aList, 3)
        elif option == "6":
            # Input: Title to search
            search = input("Please enter title to search: ")
            print()
            # This calls the function FindBy using the first index
            FindBy(search, 0)
        elif option == "7":
            # Input: Artist to search
            search = input("Please enter artist to search: ")
            print()
            # This calls the function DataSort using the second index
            FindBy(search, 1)
        elif option == "8":
            # Input: Genre to search
            search = input("Please enter genre to search: ")
            print()
            # This calls the function DataSort using the third index
            FindBy(search, 2)
        elif option == "9":
            # Input: Maximum price to search
            search = input("Please enter maximum price to search: ")
            print()
            # This calls the function DataSort using the fourth index
            FindBy(search, 3)
        elif option == "10":
            quit()
        else:
            # This prints an error message if the option menu entered is not valid
            print("Error, please enter a valid option")
            # Input: Menu option
            option = input("Please enter a menu option: ")

# Input: Name of CD database                          
CD = input("Enter name of CD database: ")

aList = CreateDatabase(CD)

# This calls the function DisplayMenu
DisplayMenu()

