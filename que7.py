def prefix_to_infix(prefix):
    stack = []
    for token in reversed(prefix.split()):
        if token.isdigit():
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            expression = '(' + operand1 + ' ' + token + ' ' + operand2 + ')'
            stack.append(expression)
    return stack[-1]

prefix_expression = "* + 2 3 5"
infix_expression = prefix_to_infix(prefix_expression)
print("Infix expression:", infix_expression)
