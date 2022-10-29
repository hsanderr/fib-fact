"""
Henrique Sander Lourenco
10802705
"""

def fact(x):
    return x * fact(x - 1) if x > 1 else 1

def fib(x):
    return fib(x - 1) + fib(x - 2) if x > 1 else 1 if x == 1 else 0

def isNumber(listItem):
    return True if (listItem != '\n') and (listItem != ' ') else False

def indexIsEven(listItem):
    return True if (listItem[0] % 2 == 0) else False

def indexIsOdd(listItem):
    return True if (listItem[0] % 2 != 0) else False

with open('input.dat', 'r') as inputFile:
    inputData = list(inputFile.read())

filteredInputData = list(filter(isNumber, inputData))
numberInputData =  list(enumerate(map(int, filteredInputData)))
evenIndexData = [data[1] for data in list(filter(indexIsEven, numberInputData))]
oddIndexData = [data[1] for data in list(filter(indexIsOdd, numberInputData))]
fibonacci = list(map(fib, evenIndexData))
factorial = list(map(fact, oddIndexData))
outputLines = ["Linha {}:\tfibonacci: {}\tfactorial: {}\n".format(i, fibonacci[i], factorial[i]) for i in range(len(fibonacci))]
outputData = ''.join(outputLines)   

with open('output.dat', 'w') as outputFile:
    outputFile.write(outputData)
