import numpy as np

def factorial(N):
    if N==1:
        return N
    else:
        return N*factorial(N-1)

def sin(x,N):
    temp=0;
    for ii in range(0,N+1):
        temp=temp+(-1)**ii/factorial(2*ii+1)*x**(2*ii+1)
    return temp

