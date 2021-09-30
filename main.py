#Learning Basics with Alpay ^-^
#I'll start with "for" loops today. 09/29/21

list = (1, 2, 3, 4, 5, 6, 7, 8)
total = 0

#Basically, on each turn elements take one number, end finishes the loop.

for element in list:
    total = total + element

print(total)

#----------------------------------------------------------------------------------#

list = (1, 2, 3, 4, 5, 6, 7, 8)
total = 0

for element in list:
    total = total + element

#We will be able to see what number element takes, and what number total gets on each turn and at last, the subtotal.

    print("total:{} , element:{}" .format(total,element))

print(total)

#----------------------------------------------------------------------------------#

str = "AlpayAllen"

for i in str:

#On python strings doesnt work so complicated as it is on C programming

    print("{}" .format(i))
    print(i * 5)

#----------------------------------------------------------------------------------#

list = [(1,2), (3,4), (5,6), (7,8)]

for (first, second) in list:

    print(first, second)

#For example, it takes first and second at the same time on each turn because, it's 2 dimensional list.

#----------------------------------------------------------------------------------#

#DICTIONARY FIRST

dictionary = {"one":1, "two":2, "three":3, "four":4, "five":5}

dictionary.keys()

#DICTIONARY SECOND

dictionary.values()

#DICTIONARY THIRD

dictionary.items()


