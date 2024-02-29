#Question 4
def removeDuplicates(lis : list):
    p = []
    for i in lis:
        if i not in p:
            p.append(i)
    print(p)

removeDuplicates([1, 1, 2, 3, 4, 4])