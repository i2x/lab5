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
def evaluateInfix(infix_exp):
    def infixToPostfix(infix_exp):
        precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        stack = []
        postfix = []
        
        for char in infix_exp:
            if char.isdigit():
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop() 
            else:
                while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(char)
        
        while stack:
            postfix.append(stack.pop())
        
        return "".join(postfix)

    def evaluatePostfix(postfix_exp):
        stack = []
        for char in postfix_exp:
            if char.isdigit():
                stack.append(int(char))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if char == '+': stack.append(val1 + val2)
                elif char == '-': stack.append(val1 - val2)
                elif char == '*': stack.append(val1 * val2)
                elif char == '/': stack.append(val1 / val2)

        return stack.pop()

    postfix_exp = infixToPostfix(infix_exp)
    result = evaluatePostfix(postfix_exp)
    return "{:.1f}".format(result)
