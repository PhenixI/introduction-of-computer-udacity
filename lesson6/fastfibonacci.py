#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    pre_2 = 0
    pre_1 = 1

    if n == 0:
        return pre_2
    if n == 1:
        return pre_1

    i = 2
    while i<=n:
        sum = pre_1+pre_2
        pre_2 = pre_1
        pre_1 = sum
        i += 1
    return sum

def fib(n):
    current = 0
    after = 1
    for i in range(0,n):
        current ,after = after , current + after

    return current
        
