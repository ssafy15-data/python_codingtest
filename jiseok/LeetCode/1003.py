class Solution:
    def isValid(self, s: str) -> bool:
        # abc 찾아서 없애고 넘기고 계속 하고 마지막에 빈 스트링이면 return true
        while s:
            abc_idx = s.find('abc')
            if abc_idx == -1:
                return False
            s = s.replace('abc', '', 1)
        return True
