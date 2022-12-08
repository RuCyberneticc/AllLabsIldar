#task2
import numpy as np

def MAINO():
 def create_new_array(arr):
  m = max((abs(e), i1, i2) for i1, l in enumerate(arr) for i2, e in enumerate(l))
  new_a = [[c for i2, c in enumerate(r) if i2 != m[2]] for  i1, r in enumerate(arr) if i1 != m[1]]
  return new_a


 def main():
    with open('/content/Ибрагимов_Ильдар_РАВИЛЬЕВИЧ_группа_У-223_vvod1.txt') as f:
     arr3 = [list(map(int, row.split())) for row in f.readlines()]
    with open('/content/Ибрагимов_Ильдар_РАВИЛЬЕВИЧ_группа_У-223_vivod1.txt', 'w') as f:
      f.write(str(create_new_array(arr3)))

 if __name__ == "__main__":
    main()
MAINO()
