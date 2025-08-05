
temp = int(input("Enter the temperature in celsius: "))  #eg=28

if temp<10:   #28<10  (False)

    print("Cold")

elif 10<=temp<20:  #28<20  (False)    # either write like this 

    print("Cool")

elif temp>=20 and temp<25:  #28<25  (False)     # or write like this using "and"

    print("Pleasant")

elif temp<30:  #28<30   (True -this condtn executes and works and then exits. The rest below wont be traversed )      # or write like this instead of ( temp>=25 and temp<30 )

    print("Warm")

elif temp<35:

    print("Hot")

else:

    print("Scorching hot")