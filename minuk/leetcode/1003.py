class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        target = ['a', 'b', 'c']
        for c in list(s):
            stack.append(c)
            while (len(stack) >= 3 and stack[-3:] == target):
                stack.pop()
                stack.pop()
                stack.pop()

        return True if not stack else False