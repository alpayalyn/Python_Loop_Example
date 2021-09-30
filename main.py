#While loop basics with Alpay 09/29/21

index = 0
list = (1, 2, 3, 4, 5)

while (index < len(list)):

    index = index + 1
#5 times it will be repeated.

    print(index)

#-----------------------------------------------------------------------------#

#range basics with Alpay 09/29/21

print(*range(0,20))

print(*range(0, 100, 2))


for i in range(1, 20):

    print(i)

#-----------------------------------------------------------------------------#

#Its going to be about listing, with Alpay.

list1 = [1, 2, 3, 4, 5]
list2 =  list () #lets add just a list

for element in list1:

    list2.append(element)

print(list1)
