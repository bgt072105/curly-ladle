def swapnumbers():
    int1 = int(input("Enter a number: "))
    int2 = int(input("Enter a second number: "))

    print("Before: num1 = {0} and num2 = {1}".format(int1, int2))
    # set a temporary variable to hold int1's value
    temp = int1
    # set int1 equal to int2
    int1 = int2
    # set int2 equal to the temporary variable that is holding int1's value
    int2 = temp
    # int1, int2 = int2, int1
    print("After: num1 = {0} and num2 = {1}".format(int1, int2))