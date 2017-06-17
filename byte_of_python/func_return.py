def maximum(x, y):
    '''Function that returns maximum number from provided arguments'''
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    return y

a = maximum(4, 10)
print(a)
