class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            stack.append(ch)
            if ch=='c' and len(stack)>=3 and (stack[-3],stack[-2])==('a','b'):
                del stack[-3:]
        return not stack