#task3
def wuw(n):
    two_sqrt = 2
    number = 1
    while two_sqrt <= n:
        two_sqrt *= 2
        number += 1
    print(number - 1, two_sqrt // 2)
wuw(int(input()))
