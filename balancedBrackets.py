"""
Given a string s containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.
"""


def check_string(input: list[str])->bool:


    stack = []
    pairs = {')':'(', '}':'{', ']':'['}

    for paren in input:
        # check if it's a closing parenthesis
        if paren in pairs:
            
            # check if it's the matching pair on the stack
            stack_top = stack.pop() if stack else None

            if pairs[paren] != stack_top:
                return False
        else:
            stack.append(paren)
    
    return (len(stack) == 0)


example = ['(','{','[',']','}',')']

example2 = ['(','(','{','(','(','(','(','(','[',']','}',')']

example3 = [']']
print(check_string(example))
print(check_string(example2))
print(check_string(example3))
