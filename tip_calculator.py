#Recursive function to get bill with valid type
def getBill():
    #Set bill equal to user input
    Bill = input("Enter Bill Total: ")
    #Exception handling and converting Bill from string to float
    try:
        #Change input to float and return Bill with no whitespace
        Bill = float(f"{Bill}\n")
        #Checks for non-infinite, positive value
        if Bill > 0 and Bill != float('inf'):
            print("Bill Total: $", Bill)
            return Bill
        else:
            print("Enter Positive, non-infinite Value for Bill")
            getBill()

    except ValueError:
        print("Input valid number for Bill")
        getBill()
getBill()


def numPeople():
    people = input("How many people are splitting the bill?")
    #Exception handling for converting people from str to int
    try:
        #Change input to integer and return with no whitespace
        people = int(f"{people}\n")
        #Checks for positive value
        if people > 0:
            print("Total People:", people)
            return people
        else:
            print("Please enter positive number of people")
            numPeople()
    except ValueError:
        print("Input valid whole number of people")
        numPeople()
numPeople()   


