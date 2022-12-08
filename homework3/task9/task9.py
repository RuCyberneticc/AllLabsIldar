#task9
def choco(n,m,k):
    if k < n*m and (k % n == 0 or k % m == 0):
        print("Да")
    else:
        print("Нет")
choco(int(input()), int(input()), int(input()))
