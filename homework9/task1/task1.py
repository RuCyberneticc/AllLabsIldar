#lab9
#task 1
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
    arr2 = np.random.randint(0,5, size = (5,5))
    print(arr2)
    k = int(input("k= "))
    count = 0
    maxx = 0
    print(find_max_array(arr2, k, maxx , count))

 if __name__ == "__main__":
    main()
MAIN()    
