
# display centuary year if year ending with 2 zeros else non-centuary


year = int(input("Enter the year: "))

if year%100 == 0:

    print("Centuary Year")

else:

    print("Non-centuary Year")