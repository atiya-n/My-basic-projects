
num = int(input("Enter the number to check whether prime or not: "))

is_prime = True

for i in range(2,num):

    if num % i ==0:

        is_prime = False

        break

# print(is_prime)  #o/p => True or False

result = "Prime number" if is_prime == True else "Not prime"

print(result)
