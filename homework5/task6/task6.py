#task6
def number(index):
    count = 0
    summa = 0
    while index != 0:
        summa += index
        count += 1
        index = int(input())
    print(summa / count)
number(int(input()))
