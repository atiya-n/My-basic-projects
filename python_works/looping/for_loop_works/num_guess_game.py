
# Guessing game

from random import randint   #imported random package to use the randint func.

target = randint(1,10)       #the range is given between 1 and 10  hence picks anyone in that range.

count = 0

while True:    #always enters the loop

    num = int(input("Guess the number: "))

    if target == num:

        print("Congratulations")

        break

    count = count+1

print(f"The number of times guessed is {count}")
