l = [2,4,5,4,7, 9, 8]


# MAP Takes a function and iterable (on which we want to apply that function) as argument

# cube = lambda x: x*x*x

# newl = list(map(cube, l))

# print(newl)

# FILTER Takes a function and iterable (on which we want to apply that function) as argument
# check = lambda a: a<4

# newl = list(filter(check, l))


# REDUCE Takes a function and iterable (on which we want to apply that function) as argument
from functools import reduce

sum = lambda x,y: x+y

newl = reduce(sum, l)

print(newl)


