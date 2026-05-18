class Solution:
    def isValid(self, s: str) -> bool:
        """
        전형적인 패턴매칭 스택문제. 이전 문자열 폭발 문제와 유사함
        """
        stack = []
        for x in s:
            if x == "c":
                if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(x)

        return not stack
