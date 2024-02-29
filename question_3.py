#Question 3
#3.1
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
for i in range(1, 26):
    if i < 6:
        list1.append(i)
    elif i < 11:
        list2.append(i)
    elif i < 16:
        list3.append(i)
    elif i < 21:
        list4.append(i)
    elif i < 26:
        list5.append(i)
final_list = [list1, list2, list3, list4, list5]
print(final_list)

#3.2
final_list_2 = []
for i in final_list:
    partial_list = []
    for q in i:
        if q % 3 == 0:
            partial_list.append('?')
        else:
            partial_list.append(q)
    final_list_2.append(partial_list)

print(final_list_2)