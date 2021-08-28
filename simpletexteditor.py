# Enter your code here. Read input from STDIN. Print output to STDOUT

numberOfOperations = input()
string = ""
lenLastOpList = 0
lastDeletedString = ""
lastOperation = 0
operationStack = []
lastDeletedStringStack = []
for count in range(int(numberOfOperations)):
    operation = input()
    opList = operation.split(" ")
    if opList[0] == '1':
        operationStack.append(opList)
        lenLastOpList = len(opList[1])
        string += opList[1]
    elif opList[0] == '2':
        operationStack.append(opList)
        k = int(opList[1])
        lastDeletedString = string[len(string)-k:len(string)]
        lastDeletedStringStack.append(lastDeletedString)
        string = string[0:len(string)-k]   
    elif opList[0] == '3':
        print(string[int(opList[1])-1])
    elif opList[0] == '4':
        lastOpItem = operationStack[len(operationStack)-1]
        if lastOpItem[0] == '1':
            string = string[0:len(string)-len(lastOpItem[1])]
        elif lastOpItem[0] == '2':
            lastDeleteString = lastDeletedStringStack.pop(len(lastDeletedStringStack)-1)
            string += lastDeleteString
        operationStack.pop(len(operationStack)-1)
    lastOperation = opList[0]
