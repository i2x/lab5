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
def InfixtoPrefix(infix_exp):
    def get_precedence(op):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence[op] if op in precedence else 0

    def infix_to_postfix(infix):
        stack = []
        postfix = ""
        for char in infix:
            if char.isalpha() or char.isdigit():
                postfix += char
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            else:
                while stack and get_precedence(char) <= get_precedence(stack[-1]):
                    postfix += stack.pop()
                stack.append(char)
        while stack:
            postfix += stack.pop()
        return postfix

    # Step 1: Reverse the infix expression
    infix_exp = infix_exp[::-1]

    # Step 2: Replace '(' with ')' and vice versa
    infix_exp = ''.join(['(' if char == ')' else ')' if char == '(' else char for char in infix_exp])

    # Step 3: Convert to postfix
    postfix_exp = infix_to_postfix(infix_exp)

    # Step 4: Reverse postfix to get prefix
    prefix_exp = postfix_exp[::-1]

    return prefix_exp