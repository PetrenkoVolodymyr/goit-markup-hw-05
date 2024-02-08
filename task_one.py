def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n==1:
            return 1
        if n==0:
            return 0
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1)+fibonacci(n-2)
            return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(15))



n = 5 #3
m = 9 #21

# a=0
# def fib(n):
#     if n==1:
#         return 1
#     if n==0:
#         return 0
#     else:
#         return (fib(n-1)+fib(n-2))
# print(f' для {m} - {fib(m-1)}')