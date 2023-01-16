def basic_calculator(x, y, operation):

    if (x.isnumeric() & y.isnumeric()):
        x = float(x)
        y = float(y)
        if operation == "+":
            result = x + y
        elif operation == "-":
            result = x - y
        elif operation == "/":
            result = x / y
        elif operation == "*":
            result = x * y
        else:
            result = "Operations supported: add, substract, divide, multiply only"
    else:
        result = "Please enter a valid number for x & y"

    return result
