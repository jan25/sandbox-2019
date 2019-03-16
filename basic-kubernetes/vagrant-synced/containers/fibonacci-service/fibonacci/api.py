
# TODO Use redis store to cache calculated values
store = {}

def fibonacci(n):
    if n < 2: return n
    if n not in store:
        store[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return store[n]
