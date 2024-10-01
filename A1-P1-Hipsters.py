#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

"""
Student Name: William Wilson
Program Title: Logic and Programming
Description: Assignment 1 Hipsters
"""
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
    welcomeMessage=print("Welcome to Hipsters Local Vinyl Records.\nWhere we keep your interests spinning faster than your record player.")
    #customers name
    customerName=input("Hipster customer please enter your name: ")
    #obtain cost of records purchased
    recordsPurchased=float(input("Please enter the cost of the records that you purchased today: "))
    #distance ex. 45km
    deliveryDistance=float(input("Please enter the distance for your spinning delivery: "))

    #distance for delivery $15 /km
    deliveryDistance=deliveryDistance*15
    #taxes records*.14
    taxCost=recordsPurchased*.14
    #add taxes to records purchased 
    recordCost=recordsPurchased+taxCost
    #Add everything to get total cost 
    totalCost=recordCost+deliveryDistance
    print("{0}, Your Hipster's Purchase costs are: \nRecords Purchased: ${1} \nPurchase Taxes: ${2:.2f} \nDelivery Fee: ${3:.2f} \nTotal Purchase Price Including Delivery is: ${4:.2f}".format(customerName, recordsPurchased, taxCost, deliveryDistance, totalCost))
    
    # YOUR CODE ENDS HERE

main()