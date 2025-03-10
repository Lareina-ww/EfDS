def rpn(tokens):
    """Evaluate an expression in RPN"""
    stack=[]
    for token in tokens:
        if token.replace('.', '', 1).replace('-', '', 1).isdigit():
            stack.append(float(token))  
        elif token in {"+", "-", "*", "/"}: 
            if len(stack) < 2:
                raise ValueError("Not enough operands for operator.")
            b = stack.pop()
            a = stack.pop()
            
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero.")
                result = a / b
            
            stack.append(result)  
        else:
            raise ValueError(f"Invalid token: {token}")
    
    if len(stack) != 1:
        raise ValueError("Too many operands remaining on stack.")
    
    return stack.pop()


import sys 

if __name__ == "__main__":  # a way to define the main part of a script
    """When script is executed, read parameters and compute RPN"""
    try:
        tokens = sys.argv[1:]  
        result = rpn(tokens)  
        print(result)  
    except Exception as e:
        print(f"Error: {e}")
