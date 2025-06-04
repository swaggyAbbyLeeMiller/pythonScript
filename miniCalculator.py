def calculator(a, b, operation):
    if (operation == "add"):
        return a + b
    elif (operation == "subtract"):
        return a - b
    elif (operation == "multiply"):
        return a * b
    elif (operation == "divide"):
        if (a ==0 or b == 0):
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: you didnt enter a valid operation bro"
    

#with user input

try: 
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    yourInput = input("Enter the operation, here are your choices: add, subtract, multiply, divide: ")

    result = calculator(num1, num2, yourInput)
    print("Here is the result: ", result)
    
    
except ValueError:
    print("Error: Please enter valid numbers.")
    
    
    

#example
# print(calculator(2, 3, "add"))