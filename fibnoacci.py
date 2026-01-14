#with recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("\nEnter number of terms: "))
print("Fibonacci series (with Recursion):")
for i in range(n):
    print(fibonacci(i), end=" ")

#with iteration

n = int(input("\nEnter number of terms: "))
a, b = 0, 1
print("Fibonacci series (with Iteration):")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
















