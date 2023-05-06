# Function to find the smallest number in a stack
def find_smallest(stack):
    if not stack:
        return None

    min_val = stack.pop()
    while stack:
        val = stack.pop()
        if val < min_val:
            min_val = val

    return min_val

# Take user input for the stack
stack = input("Enter the stack (comma separated): ").split(',')
stack = [int(i) for i in stack]

# Find the smallest number in the stack and print the result
smallest = find_smallest(stack)
if smallest:
    print("The smallest number in the stack is:", smallest)
else:
    print("The stack is empty.")
