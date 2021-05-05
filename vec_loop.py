#Why should I use vectors for ML algorithms instead of for loops
import numpy as np
import time

n = 10000000
#Defining two random vectors
a = np.random.rand(n)
b = np.random.rand(n)

# numpy vector dot version
tic = time.time()
c = np.dot(a,b)
toc = time.time()

print(c)
print("Vectorized version (ms):" + str(1000*(toc - tic)))

c = 0
# For loop version

tic = time.time()
for i in range (n):
    c += a[i] * b[i]
toc = time.time()

print(c)
print("For loop version (ms):" + str(1000*(toc - tic)))
