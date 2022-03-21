# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def fac_tester():
    try:
        num = int(input("Enter a number for factorial: "))
        # check if the number is negative
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
        else:
            print("The factorial of", num, "is", recur_factorial(num))
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    fac_tester()