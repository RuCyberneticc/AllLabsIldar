#task2
def wuw(n):
    i = 1
    sp=[]
    while i <= n:
        i = i + 1
        if n % i == 0:
            sp.append(i)
    print(min(sp))
wuw(int(input()))
