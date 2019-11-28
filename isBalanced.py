import time
"""
By this logic, we say a sequence of brackets is balanced if the 
following conditions are met:
1. It contains no unmatched brackets.
2. The subset of brackets enclosed within the confines of a matched pair of 
brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of 
brackets is balanced. If a string is balanced, return YES. 
Otherwise, return NO.
"""
"""
1. create an object where key value pair are opening and closing brackets
2. create an stack (cache) to push opening brackets
3. loop through string
    a. if opening bracket push to cache
    b. if not closing bracket pop from cache 
    c. if poped bracket not in value pair return `NO`
"""
class Stack:

        def __init__(self):
            self.storage = []

        def push(self, value):
            self.storage.append(value)

        def pop(self):
        # if stack is empty return None
            if not self.storage:
                return None

            return self.storage.pop()

        def length(self):
            return len(self.storage)

def isBalanced(s):
    stack = Stack()
    brackets_pairs = {")": "(", "]": "[", "}": "{"}

    for bracket in s:
        if bracket in '({[':
            stack.push(bracket)
        else:
            open_brace = stack.pop()
            if open_brace is not brackets_pairs[bracket]:
                return "NO"
    if stack.length():
        return "NO"
    return "YES"

""" 
throws runtime error if stack data structure
is not used
"""
def isBalanced_2(s):

    brackets_pairs = {")": "(", "]": "[", "}": "{"}
    cache = []
    for bracket in s:
        if bracket in '({[':
            cache.append(bracket)
        else:
            open_brace = cache.pop()
            if open_brace is not brackets_pairs[bracket]:
                return "NO"
    if len(cache):
        return "NO"
    return "YES"

start_time = time.time()
isBalanced('{[()]}')
isBalanced('{[(])}')
isBalanced('{(([])[])[]}[]')
isBalanced('{(([])[])[]}')
end_time = time.time()
print(f"Stack runtime: {end_time - start_time} seconds")

start_time = time.time()
isBalanced_2('{[()]}')
isBalanced_2('{[(])}')
isBalanced_2('{(([])[])[]}[]')
isBalanced_2('{(([])[])[]}')
end_time = time.time()
print(f"List runtime: {end_time - start_time} seconds")