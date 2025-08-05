#A shopkeeper purchase a prdt at 'x' rupees and sold the product at a profit of y%. 
# Find the selling price.

# gst= 8% of selling price

purchase_price = int(input("Enter the purchase price: "))

profit_perc = int(input("Enter the profit %: "))

profit = (profit_perc/100)*purchase_price

selling_price = purchase_price + profit    #selling price without gst

GST = 8

gst_amount = (GST/100)*selling_price

total_price = selling_price + gst_amount   #added gst

print("Total selling price =",total_price)


