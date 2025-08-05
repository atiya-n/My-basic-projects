
# read the bill amount

# read the tip amount

# read the no of dines

# print individual split

bill_amount = int(input("Enter the bill amount: "))

tip_amount = int(input("Enter the tip amount: "))

dines = int(input("Enter the number of dines: "))

split = (bill_amount+tip_amount)/dines

print("Individual split =",split)