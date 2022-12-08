#task7
def YearQualifier(x):
 if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print("Да")
 else:
    print("Нет")
YearQualifier(int(input())) 
