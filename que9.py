def reverse_stack(stack):
    if len(stack) <= 1:
        return stack
    else:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

# Take user input for the stack
stack = input("Enter the stack (comma separated): ").split(',')
stack = [int(i) for i in stack]

print("Original stack:", stack)

# Reverse the stack and print the result
reverse_stack(stack)
print("Reversed stack:", stack)
