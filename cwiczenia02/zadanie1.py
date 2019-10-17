# Zadanie 1


def take_index(a_list, b_list):
    result = []
    for i in range(len(a_list)):
        if i % 2 == 0:
            result.append(i)
    for i in range(len(b_list)):
        if i % 2 != 0:
            result.append(i)
    return result


list1 = [25, 35, 45, 55]
list2 = [100, 120, 140]
list3 = take_index(list1, list2)
print("Wynik:", list3)
