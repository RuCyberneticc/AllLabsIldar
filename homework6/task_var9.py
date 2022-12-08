#lab6
def searcher(string, search):
 count = 0
 for i in range(len(string)):
  if string[i: i + len(search)] == search:
   count += 1
 return(count)
searcher(str(input('Введите строку, в которой будем искать: \n')),search = str(input('Введите что искать: \n')))
