#task3
def Calc(n):
 minutes = n
 hours = minutes // 60
 minutes = n % 60
 if n < 1440:
    print(hours, ":", minutes)
 else:
    days = hours // 24
    hours %= 24
    print(days, 'суток/сутки', hours, ':', minutes)
Calc(int(input("Количество минут: ")))
