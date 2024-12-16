#def fibo(num):
#    if num < 2:
#       return num
#   else:
#       return fibo(num-1) + fibo(num-2)
from math import sqrt

def fibo(num):
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2

    return round((phi**num - psi**num) /sqrt(5))

print(fibo(5))
