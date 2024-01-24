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

def is_operand(c):
    """
    Return True if the given char c is an operand, e.g. it is a number
    """
    return c.isdigit()
    
def evaluatePrefix(expression):
    """
    Evaluate a given expression in prefix notation.
    Asserts that the given expression is valid.
    """
    stack = []
 
    # iterate over the string in reverse order
    for c in expression[::-1]:
 
        # push operand to stack
        if is_operand(c):
            stack.append(int(c))
 
        else:
            # pop values from stack can calculate the result
            # push the result onto the stack again
            o1 = stack.pop()
            o2 = stack.pop()
 
            if c == '+':
                stack.append(o1 + o2)
 
            elif c == '-':
                stack.append(o1 - o2)
 
            elif c == '*':
                stack.append(o1 * o2)
 
            elif c == '/':
                stack.append(o1 / o2)
 
    result = stack.pop()
    return "{:.1f}".format(round(result, 1))  # Format result with one decimal place
