#task9
def Fib(n):
    a = 1
    b = 0
    sum = 0
    for i in range(1, n + 1):
        x = a
        a = x + b
        b = x
        sum += x
    print(sum)
Fib(int(input()))
