#!/usr/bin/env python 3

# Suite de Fibonnaci : Un+2 = Un+1 + Un
# U0 = 0 U1 = 1

# RECURSIVE

def fibonacci_rec_naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rec_naive(n-1) + fibonacci_rec_naive(n-2)

print(fibonacci_rec_naive(10))

# INTERATIVE

def fibonacc_inter(n):
    u0 = 0
    u1 = 1
    for i in range(n-1):
        u2 = u0 + u1
        temp = u1
        u1 = u2
        u0 = temp
        return u2

print(fibonacc_inter(20))