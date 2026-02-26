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