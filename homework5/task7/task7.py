#task7
def none(index):
    number = 0
    while index != 0:
        index1 = int(input())
        if index < index1 and index1 != 0:
            number += 1
        index = index1
    print(number)
none(int(input()))
