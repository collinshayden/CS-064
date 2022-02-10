#Hayden Collins
#CS 064
#an attempt to avoid proving what seems like a hard number theory problem

import timeit
from math import sqrt
start = timeit.default_timer()

squares = []

for i in range(1,100000):
    square = i*i
    squares.append(square)
    half_square = square/2
    if half_square in squares:
        print(half_square)
        break
        
stop = timeit.default_timer()
print(f"Time elapsed: {stop-start}")