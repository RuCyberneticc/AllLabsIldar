#task4
def shnur(a,b,l,N):
     lenght = 2 * l + (2 * N - 1) * a + 2 * (N - 1) * b
     return(lenght)
print("Искомая длина шнурка: ",shnur(int(input()),int(input()),int(input()),int(input())))
