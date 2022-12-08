#task8
def equally(n):
    count = 0
    mini = -1
    maxi = 0
    while n != 0:
        if mini == n:
            count = count + 1
        else:
            mini = n
            maxi = max(maxi, count)
            count = 1
        n = int(input())
    maxi = max(maxi,count)
    print("Максимально подряд: ", maxi)
equally(int(input()))
