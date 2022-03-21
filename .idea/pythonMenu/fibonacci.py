

def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n-1) + recur_fibonacci(n-2)

def fib_tester():
    try:
        num = int(input("Enter a number for fibonacci: "))
        if num == 0:
            print("invalid")
        else:
            print("Fibonacci Sequence:")
            for i in range(num):
                print(recur_fibonacci(i))
    except ValueError:
        print("invalid")

if __name__ == "__main__":
    fibonacci_tester()