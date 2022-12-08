#task4
def sport(x,y):
    day = 1
    while x < y:
        x *= 1.1
        day += 1
    print(day)
sport(int(input()),int(input()))
