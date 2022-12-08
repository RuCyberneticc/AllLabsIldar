#task6
def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    print(fac)
factorial(int(input()))
