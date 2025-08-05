# calculate bill amount
# calculate no of dines
# calculate tip as 12% of the bill amount
# calculate gst as 8% of the bill amount
# calculate total amount and individual split

bill_amount = int(input("Enter the bill amount: "))

dines = int(input("Enter the no of dines: "))

tip_amount = (12/100) * bill_amount

gst = (8/100) * bill_amount

total_amount = bill_amount + tip_amount + gst

individual_split = total_amount/dines

print("Total bill amount =",total_amount)

print("Individual split =",individual_split)

