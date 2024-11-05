#Two numbers and an operator are given. 
#Define a function f(number1,number2,operator) that returns the result of an arithmetic operation. 
#The available operators are +,-,*,%,**. Sample result:
def f(number1,number2,operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2
    else:
        return "nuhh uhhh"
   