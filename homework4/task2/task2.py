#task2 
def number(a,b):
    numbers = []
    if a < b:
        for i in range(a, b+1):
            numbers.append(i)
        print(numbers)
    else:
        for i in range(b, a + 1):
            numbers.append(i)
            numbers.sort(reverse=True)
        print(numbers)
number(int(input()),int(input()))
