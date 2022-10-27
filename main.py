"""
Henrique Sander Lourenco
10802705
"""

def fact(x):
    return x * fact(x - 1) if x > 1 else 1

def fib(x):
    return fib(x - 1) + (x - 2) if x > 1 else 1 if x == 1 else 0

def isNumber(element):
    return True if (element != '\n') and (element != ' ') else False

def separateELements(numList):

with open('input.dat') as inputFile:
    inputData = list(inputFile.read())
    filteredInputData = list(filter(isNumber, inputData))
    numberInputData =  list(map(int, filteredInputData))
    print(filteredInputData)

#for element in filteredInputData:
#    if i % 2 == 0:
#        if 'thisList'



#with open('')


l1 = [2, 5, 3, 4, 1, 0]
l2 = [3, 1, 4, 2, 0, 5]

res1 = map(fib, l1)
res2 = map(fact, l2)

print(list(res1))
print(list(res2))
