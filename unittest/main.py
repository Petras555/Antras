def suma(a, b, c):
    return a + b + c

def list_suma(listas):
    sum = 0
    for i in listas:
        sum += i
    return sum

def max(*args):
    result = max(args)
    return result

print(max(15, 6, 0, -5))

