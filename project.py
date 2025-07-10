def factorial(n):
    if n < 0:
        return None  # Factorial not defined for negative numbers
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci_series(count):
    series = []
    a, b = 0, 1
    for _ in range(count):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}")
    fib_count = int(input("Enter the number of Fibonacci terms: "))
    print(f"Fibonacci series ({fib_count} terms): {fibonacci_series(fib_count)}")