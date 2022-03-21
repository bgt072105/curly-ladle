

def recur_fibonacci(n):
    # logic for how the fibonacci sequence is made
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n-1) + recur_fibonacci(n-2)

def fib_tester():
    try:
        num = int(input("Enter a number for fibonacci: "))
        # fibonacci sequence cannot end in 0
        if num == 0:
            print("invalid")
        # print the list of all numbers in that fibonacci sequence
        else:
            print("Fibonacci Sequence:")
            for i in range(num):
                print(recur_fibonacci(i))
    except ValueError:
        print("invalid")

if __name__ == "__main__":
    fib_tester()