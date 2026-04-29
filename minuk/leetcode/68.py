class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        slicing_pos = [0]
        now_length = -1
        for i in range(len(words)):
            if (now_length + len(words[i]) + 1 > maxWidth):
                slicing_pos.append(i)
                now_length = -1
            now_length += len(words[i]) + 1
        slicing_pos.append(len(words))
        res = []
        for i in range(len(slicing_pos) - 1):
            x, y = slicing_pos[i], slicing_pos[i + 1]
            count = 0
            for j in range(x, y):
                count += len(words[j])
            required_count = maxWidth - count
            strings = []
            words_count = y - x - 1
            for j in range(x, y):
                strings.append(words[j])
                if (j != y - 1):
                    if (y != slicing_pos[-1]):
                        strings.append(' ' * ((required_count // words_count) + (1 if j - x < required_count % words_count else 0)))
                    else:
                        strings.append(' ')
            res.append((''.join(strings)).ljust(maxWidth))
        return res