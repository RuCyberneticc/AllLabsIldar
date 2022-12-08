# задание 4
seconds = int(input("Введите количество секунд: "))
days = seconds // 86400
seconds = seconds - days * 86400
hours = seconds // 3600
seconds = seconds - hours * 3600
minutes = seconds // 60
seconds = seconds - minutes * 60
s = seconds
print(days, ":", hours, ":", minutes, ":", s)
