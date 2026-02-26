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

def clowining():
    print("you have been clowned hehe")
    
def numbers(a):
    return [i*i for i in range(a)]