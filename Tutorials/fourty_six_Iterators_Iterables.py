import itertools
x = [1, 2, 3, 4] #iterable

n = itertools.cycle(x) # This is iterator but also iterable

y = itertools.cycle(x) 

next(y)

for i in y:
    print(i)

for i in y:
    print(i)