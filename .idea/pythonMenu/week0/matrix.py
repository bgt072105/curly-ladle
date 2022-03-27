def matrixprint(matrix):
    # This is looping over the lists in matrix. The indexes go from 0 to len - 1
    for x in matrix:
        rowString = ""
        # This is a nested for loop that is looping over the numbers in each list
        for y in x:
            rowString += str(y)+ " "
        print(rowString)

def keypad():
    matrixprint([[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]])