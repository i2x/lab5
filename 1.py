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
        
def PrefixtoPostfix(prefix_exp):
    stack = []
    
    # Start from the right end of the prefix expression
    for i in range(len(prefix_exp) - 1, -1, -1):
        # If symbol is an operand
        if prefix_exp[i].isdigit() or prefix_exp[i].isalpha():
            stack.append(prefix_exp[i])
        # If symbol is an operator
        else:
            # Pop two elements from stack
            op1 = stack.pop()
            op2 = stack.pop()
            # Concatenate them as per postfix notation
            stack.append(op1 + op2 + prefix_exp[i])

    # The remaining element in stack is the postfix expression
    return ''.join(stack)