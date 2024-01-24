class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""

    def __len__(self):
        """Return the number of elements in the stack."""

    def is_empty(self):
        """Return True if the stack is empty."""

    def push(self, e):
        """Add element e to the top of the stack."""

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        
    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """

def InfixtoPostfix(infix_exp):
    # Define precedence of operators
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    # Initialize empty stack and postfix expression
    stack = []
    postfix_exp = ''

    # Iterate through each character in the infix expression
    for char in infix_exp:
        if char not in precedence and char not in '()':  # Operand (including numeric)
            postfix_exp += char
        elif char == '(':  # Opening parenthesis
            stack.append(char)
        elif char == ')':  # Closing parenthesis
            while stack and stack[-1] != '(':
                postfix_exp += stack.pop()
            stack.pop()  # Pop the opening parenthesis
        else:  # Operator
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                postfix_exp += stack.pop()
            stack.append(char)

    # Pop any remaining operators from the stack
    while stack:
        postfix_exp += stack.pop()

    return postfix_exp