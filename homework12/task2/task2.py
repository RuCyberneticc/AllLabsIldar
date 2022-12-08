#task2
def max_rec(m = None):
    inp = int(input())
    if inp == 0:
        return m
    else:
        if m is None:
            return max_rec(inp)
        else:
            return max(inp, max_rec(m))
 
print(max_rec())
