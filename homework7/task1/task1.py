#lab7
#task1
import sys
def prompt(n):
 array = [int(input()) for i in range (n)]
 array_copy = array.copy()
 minimum = sys.maxsize
 for i in range(len(array_copy)):
     if (array_copy[i] < 0):
         array_copy[i] = array_copy[i] * (-1)
 for i in range(len(array_copy)):
     if (array_copy[i] < minimum):
         minimum = array_copy[i]
 print("Минимальный по модулю элемент:")
 print(minimum)

 print("Массив в обратном порядке:")
 while n:
     print(array[n - 1],end = ' ')
     n -= 1
prompt(int(input("Введите N:")))     
