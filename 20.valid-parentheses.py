class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for (_, value) in enumerate(s):
            if len(stack) == 0:
                if value in ")}]":
                    return False
                else:
                    stack.append(value)
            elif stack[-1] == '(':
                if value in "[{(":
                    stack.append(value)
                elif value == ")":
                    stack.pop()
                else:
                    return False
            elif stack[-1] == '[':
                if value in "[{(":
                    stack.append(value)
                elif value == "]":
                    stack.pop()
                else:
                    return False
            elif stack[-1] == '{':
                if value in "[{(":
                    stack.append(value)
                elif value == "}":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0