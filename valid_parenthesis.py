class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == '[':
                stack.append('[')
            elif c == '{':
                stack.append('{')
            elif c == '(':
                stack.append('(')
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
            
        return (len(stack) == 0)
                


print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)]"))
print(Solution().isValid("{[]}"))
print(Solution().isValid("["))
print(Solution().isValid("[]]"))