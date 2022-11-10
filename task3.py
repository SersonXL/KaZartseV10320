def fib(N):
    a,b = 0, 1
    for i in range(N):
        yield a
        a,b = b, a +b
x = list(fib(10))
print(x)