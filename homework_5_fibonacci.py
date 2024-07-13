def caching_fibonacci ():
    cache = {}  # Створюємо словник для зберігання результатів 
    
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    
    return fibonacci

     
fib = caching_fibonacci()

# Приклад використання
print(fib(5))
print(fib(10))  
print(fib(15))  
print(fib(20)) 
print(fib(25)) 
print(fib(30)) 