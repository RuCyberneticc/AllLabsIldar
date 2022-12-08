#lab12
# task 1
def remaind(x, y):
    return remaind(x-y, y) if x >= y else x
remaind(int(input("Введите первое число ")),int(input("Введите второе число ")))    
