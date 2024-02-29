#Question 2
#2.1

list_50 = []
for i in range(51):
    list_50.append(i)

#2.2

def squareList(x: list):
    new_list = []
    for i in x:
        new_list.append(i**2)
    print(new_list)
    return new_list

squareList(list_50)

#2.3
listA = []
for i in range(1 , 11):
    listA.append(i)

listB = []
for i in range(20 , 31):
    listB.append(i)

listC = []
for i in listA:
    if (i % 2) == 1:
        listC.append(i)
for i in listB:
    if (i % 2) == 1:
        listC.append(i)

print(listC)