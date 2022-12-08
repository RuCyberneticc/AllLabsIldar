#task3
def number(a,b):
  if a > b:
    for i in range(a - (a + 1) % 2, b - (b % 2), -2):
        print(i, end=" ")
  else: 
    print("Некорректный ввод, первое число должно быть больше второго")
number(int(input()),int(input()))
