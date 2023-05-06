def postfix_to_prefix(postfix):
    stack = []
    for token in postfix.split():
        if token.isdigit():
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            expression = token + ' ' + operand1 + ' ' + operand2
            stack.append(expression)
    return stack[-1]

postfix_expression = "2 3 + 5 *"
prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix expression:", prefix_expression)
