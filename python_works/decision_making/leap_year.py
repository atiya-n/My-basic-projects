
# for leap year we should check for centuary year and non centuary year
# to check for leap year in centuary year => year%100 == 0 (centuary or not) and year%400 == 0 (leap or not)
# to check for leap year in non-centuary year => year%100 != 0 (not centuary year) and year%4 == 0 (leap or not)


year = int(input("Enter the year: "))

if year%100 == 0 and year%400 == 0 or year%100 != 0 and year%4 == 0:

    print(year,"is a leap year")

else:

    print(year,"is not a leap year")
