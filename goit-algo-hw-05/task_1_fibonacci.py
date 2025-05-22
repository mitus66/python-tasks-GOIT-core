"""
Creates and returns a fibonacci function that uses a cache
to store and reuse computed Fibonacci values.
"""

# INPUT  n (int): Індекс числа Фібоначчі (n >= 0).
# OUTPUT int: n-те число Фібоначчі
def caching_fibonacci():
    cache = {}
    # Обчислює n-те число Фібоначчі, використовуючи кешування
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

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

# It works!
