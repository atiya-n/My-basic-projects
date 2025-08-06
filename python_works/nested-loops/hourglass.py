
# diaplay=>
# * * * * *
#  * * * *
#    * *
#     *
#    * *
#  * * * *
# * * * * *

for row1 in range(1,5):

    for sp1 in range(1,row1+1):

        print(" ",end="")

    for col1 in range(1,6-row1):

        print("*",end=" ")

    print()

for row2 in range(2,5):

    for sp2 in range(1,5-row2):

        print(" ",end="")

    for col2 in range(1,row2+1):

        print("*",end=" ")

    print()