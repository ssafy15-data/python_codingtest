from collections import deque
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        res = []
        while i < len(words):
            width = 0  # 공백 제외한 단어 길이만의 합
            dq = deque()  # 단어 담을 queue
            # 현재 단어 길이 + 다음 단어 길이 + 단어 사이에 들어갈 최소 공백 수(각 1칸)이 maxWidth 보다 작은 경우만
            while i<len(words) and width+len(words[i])+len(dq)<=maxWidth:
                width += len(words[i])
                dq.append(words[i])
                i += 1

            spaces = maxWidth - width  # 단어 길이만을 뺀 총 공백 수
            s = ""
            word_len = len(dq)  # 단어 개수

            if i == len(words):  # 마지막 줄인 경우
                while len(dq) > 1:
                    s += dq.popleft() + " "
                s += dq.popleft()
                s += " " * (spaces-(word_len-1))  # 총 공백 수 - 단어 사이 최소 공백 수

            elif word_len == 1:  # 단어가 하나인 경우
                s += dq.popleft() + " " * spaces

            else:  # 그 외의 경우: 왼쪽 정렬하지 않는 경우
                space = spaces // (word_len-1)  # 각 단어 사이에 똑같이 들어갈 최소 공백 수
                extra_space = spaces % (word_len-1)  # 남은 공백 수: 왼쪽부터 하나씩 더 줄 것임
                # 단어 사이 개수만큼 반복
                for j in range(word_len-1):
                    s += dq.popleft() + (" " * space)
                    s += " " * (1 if j < extra_space else 0)  # extra_space가 남아있으면 1칸씩 추가 공백
                s += dq.popleft()

            res.append(s)

        return res