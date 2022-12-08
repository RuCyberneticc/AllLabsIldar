#task5 
def minOfThree(a,b,c):
 smallest = 0

 if a < b and a < c :
    smallest = a
 if b < a and b < c :
    smallest = b
 if c < a and c < b :
    smallest = c
 return (smallest)
print("Наименьшим из 3 чисел является: ", minOfThree(int(input()),int(input()),int(input())))
