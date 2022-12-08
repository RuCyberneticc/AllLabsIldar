#lab12
# task 1
def remaind(a, b):
    return remaind(a-b, b) if a >= b else a
remaind(int(input("Введите первое число ")),int(input("Введите второе число ")))    
