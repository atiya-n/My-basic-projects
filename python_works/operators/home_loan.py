
loan_amount = int(input("Enter the loan amount: "))

interest = int(input("Enter the interest: "))

loan_tenure = int(input("Enter the loan tenure in years: "))

loan_tenure_months = loan_tenure*12

interest_monthly = interest / (loan_tenure_months*100)

EMI = (loan_amount*interest_monthly*(1+interest_monthly)**loan_tenure_months) / ((1+interest_monthly)**loan_tenure_months -1)

interest_payable = EMI - (loan_amount/loan_tenure_months)

total_payment = loan_amount + interest_payable

print("Monthly EMI =",EMI)

print("Total interest payable =",interest_payable)

print("Total payable amount =",total_payment)
