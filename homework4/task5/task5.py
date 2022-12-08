#task5
def stepen(n):
    sum = 0
    for i in range(1, n+1):
        znach = i**3
        sum += znach
    print(sum)
stepen(int(input()))
