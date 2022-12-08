#task8
def ladder(n):
    for i in range(n+1):
        for q in range(1, i+1):
            print(q, end=" ")
        print()
ladder(int(input()))
