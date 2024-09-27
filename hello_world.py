n = 10
i = 1

import sys

for i in range(1, n+1):
    print(i, end='')
    if i < n:
        print(" ", end='')
    else:
        print("")

for i in range(1, n+1):
    if i % 2 == 1:
        print(int((i+1)/2), end='')
    else:
        print('*', end='')
    if i < n:
        print(" ", end='')
    else:
        print("")

for i in range(1, n+1):
    print(i*2-1, end='')
    if i < n:
        print(" ", end='')
    else:
        print("")

for i in range(1, n+1):
    print(i*2, end='')
    if i < n:
        print(" ", end='')
    else:
        print("")

for i in range(1, n+1):
    print(i*3, end='')
    if i < n:
        print(" ", end='')
    else:
        print("")

for i in range(1, n+1):
    print(i*i, end='')
    if i < n:
        print(" ", end='')
    else:
        print("")

j = 0
k = 1

for i in range(1, n+1):
    if i == 1:
        print(j, end='')
    else:
        print(j+k, end='')
        j += k
        k = j - k
    if i < n:
        print(" ", end='')
    else:
        print("")

for i in range(1, n+1):
    if i % 2 == 1:
        print(int((i+1)/2), end='')
    else:
        print(i, end='')
    if i < n:
        print(" ", end='')
    else:
        print("")
