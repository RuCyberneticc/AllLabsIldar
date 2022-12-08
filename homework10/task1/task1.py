#lab10
#task1
import numpy as np
def MAIN():
 def find_max_array(arr, k, maxx, count):
    for i in range(len(arr)):
     for j in range(len(arr[0])):
         if(arr[i][j]%k==0):
            count += 1
            if(arr[i][j]>maxx):
               maxx = arr[i][j]
    return count, maxx 

 def main():
    with open('/content/Ибрагимов_Ильдар_РАВИЛЬЕВИЧ_группа_У-223_vvod.txt') as f:
     arr2 = [list(map(int, row.split())) for row in f.readlines()]
    k = int(input("k= "))
    count = 0
    maxx = 0
    with open('/content/Ибрагимов_Ильдар_РАВИЛЬЕВИЧ_группа_У-223_vivod.txt', 'w') as f:
     f.write(str(find_max_array(arr2, k, maxx , count)))

 if __name__ == "__main__":
    main()
MAIN()    
