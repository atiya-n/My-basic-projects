
# GCD or HCF of 2 nos

num1 = int(input("Enter the 1st num: "))

num2 = int(input("Enter the 2nd num: "))

limit = min(num1,num2)

gcd = 1


for i in range (1,limit+1):

    if num1 % i == 0 and num2 % i == 0:

        gcd = i

print(gcd)



