class Calculator:

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        assert y != 0   # Ajout d'une exception lors d'une division par 0
        return x / y

    def power(x, y):    
        assert isinstance(y, int)   # Ajout d'une exception si l'exposant n'est pas entier
        result = 1
        for i in range(abs(y)):
            result *= x
        if y < 0:       # Si l'exposant est négatif, on retourne 1/x^abs(y)
            result = 1 / result
        return result

    def square_root(x):
        assert isinstance(x, int)   # Ajout d'une exception si le paramètre n'est pas entier
        assert x >= 0   # Ajout d'une exception si le paramètre est négatif
        if x == 0 or x == 1:
            return x
        val = x
        precision = 0.0000001
        while abs(val - x / val) > precision:
            val = (val + x / val) / 2
        return val

def calculate(operation, x, y):
    if operation == "add":
        result = Calculator.add(x,y)
    elif operation == "substract":
        result = Calculator.subtract(x,y)
    elif operation == "multiply":
        result = Calculator.multiply(x,y)
    elif operation == "divide":
        result = Calculator.divide(x,y)
    elif operation == "power":
        result = Calculator.power(x,y)
    elif operation == "square_root":
        result = Calculator.square_root(x)
    return result

# operation = input("Enter the operation you would like to perform (add, subtract, multiply, divide, square_root, power): ")
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# print(calculate(operation, num1, num2))