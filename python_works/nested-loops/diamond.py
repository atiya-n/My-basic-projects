
# display=>
#            *
#          *   *
#        *   *   *
#      *   *   *   *
#        *   *   *
#          *   *
#            *

for row in range(1,7):

    for sp in range(1,7-row):

        print(" ",end="")

    for col in range(1,row+1):

        print("*",end=" ")

    print()

for row in range(1,7): 

    for sp in range(1,row+1):

        print(" ",end="")

    for col in range(1,7-row):

        print("*",end=" ")

    print() 
