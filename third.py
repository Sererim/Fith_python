# Создайте функцию генератор чисел Фибоначчи

def Fibonacci(n: int) -> int | list[int]:
    fib: list[int] = [0, 1]
    
    if n == 0:
        return 0
    elif n == 1:
        return fib
    else:
        [fib.append(fib[i + 1] + fib[i]) for i in range(n)]
        return fib


if __name__ == "__main__":
    print(Fibonacci(2))
    print(Fibonacci(10))
