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
            return getBill()

    except ValueError:
        print("Input valid number for Bill")
        return getBill()

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
            return numPeople()
    except ValueError:
        print("Input valid whole number of people")
        return numPeople()

def percentTip():
    #Set tip equal to user input
    Tip = input("% Tip:")
    #Exception handling and converting tip from string to float
    try:
        #Change input to float and return tip with no whitespace
        Tip = float(f"{Tip}\n")
        #Checks for non-infinite, positive value
        if Tip > 0 and Tip != float('inf'):
            print("Tip Percent: %", Tip)
            return Tip
        else:
            print("Enter Positive, Non-Infinite Value for Tip")
            return percentTip()

    except ValueError:
        print("Input valid number for tip")
        return percentTip()

#Set Functions as Variables to be Passed into Last Function
bill = getBill()
people = numPeople()
tip = percentTip()

def splitBill(bill, people, tip):
    tipAmount = bill*(tip/100)
    eachTip = round(tipAmount/people, 2)
    print(f"Each person should tip ${eachTip}")
    return eachTip

splitBill(bill, people, tip)