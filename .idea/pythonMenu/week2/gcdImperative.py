def gcdImperative(a,b):
    # return 0 for the GCD if one of the inputs is 0
    if a==0:
        return 0
    # return 0 for the GCD if one of the inputs is 0
    if b==0:
        return 0
    #  checking if the two inputs evenly divide
    if a % b ==0:
        return b
    if b % a ==0:
        return a
    # subtract smaller input from larger input. Replace larger value with difference and recursively call
    if a > b:
        return gcdImperative(a-b,b)
    if b > a:
        return gcdImperative(b-a,a)


def GCD_Imperative_tester():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    print("GCD: ", gcdImperative(num1,num2))