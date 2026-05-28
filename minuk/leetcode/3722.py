class Solution:
    def lexSmallest(self, s: str) -> str:
        char_list = list(s)
        string_list = []
        for i in range(1, len(s) + 1):
            string_list.append(''.join(reversed(char_list[:i])) + ''.join(char_list[i:]))
            string_list.append(''.join(char_list[:i]) + ''.join(reversed(char_list[i:])))
        return sorted(string_list)[0]