def calcule(num1, operator, num2):
    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    else:
        print("Opérateur invalide")
        return result
    
    print(calcule(8, '+', 4))
    print(calcule(8, '-', 4))
    print(calcule(8, '*', 4))
    print(calcule(8, '/', 4))
    print(calcule(8, '%', 4))