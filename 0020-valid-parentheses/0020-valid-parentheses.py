class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == '(' or p == '{' or p == '[':
                stack.append(p)
            elif len(stack) > 0:
                if ((p == ')' and stack[-1] != '(') or 
                    (p == ']' and stack[-1] != '[') or
                    (p == '}' and stack[-1] != '{')):
                    return False
                else:
                    stack.pop() # brackets match
            else:
                return False # stack empty with closing bracket
        return len(stack) == 0