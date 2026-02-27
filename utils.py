#Added utils.py
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
def num_gcd(n, m):
    while m:
        n, m = m, n%m
    return n

def is_it_prime(n):
    if n<2:
        return False
    for i in range(2, int(n//2)+1):
        if n%i==0:
            return False
    return True

def is_it_even(n):
    return n%2==0

def is_power_of_five(n):
    if n<1:
        return False
    while n%5==0:
        n=n//5
    return n==1
def n_of_fibonacci(n, k1=0, k2=1, t=2):
    if n == k1:
        return 1
    else:
        if n == k2:
            return t
        else:
            return n_of_fibonacci(n, k2, k1+k2, t+1)


