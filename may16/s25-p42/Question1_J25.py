global stack,TopOfStack
stack = []
for i in range(20):
    stack.append("-1")
TopOfStack = -1
def push(data):
    global stack,TopOfStack
    if TopOfStack == 19:
        return -1
    else:
        stack[TopOfStack] = data
        TopOfStack +=1
        return 1
    
def pop():
    global stack,TopOfStack
    if TopOfStack == -1:
        return -1
    else:
       ReturnValue = stack[TopOfStack]
       TopOfStack -= 1
       return ReturnValue
def ReadData(FileName): 
    global stack,TopOfStack
    try: 
        File = open(FileName) 
        for Line in File: 
            ReturnValue = push(Line.strip()) 
            if ReturnValue == -1: 
                print("Stack full") 
        File.close() 
    except: 
        print("Cannot open file")
def Calculate(): 
    global stack,TopOfStack
    Total = pop() 
    Total = int(Total) 
    Return = 0 
    LastOperator = "" 
    Operator = True 
    while(Return != -1): 
        if Operator == False: 
            Data = int(Return) 
            if LastOperator == "+": 
                Total = Total + Data 
            elif LastOperator == "-": 
                Total = Total - Data 
            elif LastOperator == "*": 
                Total = Total * Data 
            elif LastOperator == "/": 
                Total = Total / Data 
            elif LastOperator == "^": 
                Total = Total ** Data 
            Operator = True 
        else: 
            LastOperator = Return 
            Operator = False 
    return Total
ReadData("StackData.txt")
Calculate()
ReadData("SecondStack.txt")
Calculate()
print()