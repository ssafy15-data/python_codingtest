class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        lines = []
        temp_idx = 0
        len_words = len(words)
        is_break = False

        # 단어들을 순회하며, 길이 조건을 충족하는지 검사함
        # 길이를 누적하다가, 현재 단어를 포함할 경우 길이를 초과한다면, 현재 인덱스를 저장해놓고 문장처리함
        # (생각해보니 그냥 단어끼리 묶어놓는거 따로, 문장처리하는거 따로 했으면 기능분리가 가능했을텐데...)

        while True:
            is_again = False

            ## 단어 조합 파트
            line = []
            length = 0 # 단어 사이 공백 1개 포함 전체 길이
            for idx in range(temp_idx, len_words):
                word = words[idx]
                if length == 0: # 첫 단어인 경우
                    if len(word) >= maxWidth - 1:
                        temp_idx = min(len_words-1, idx+1)
                        length = len(word)
                        line.append(word)
                        break
                    else:
                        length += len(word)
                        line.append(word)
                
                else: # 첫 단어가 아닌 경우
                    if length + 1 + len(word) > maxWidth:
                        temp_idx = idx
                        is_again = True
                        break
                    else:
                        # 앞 단어와의 최소 공백까지 length에 추가
                        length += len(word) + 1
                        line.append(word)
            

            # while문 종료조건: 마지막 글자까지 순회한 경우
            # 그러나 마지막 글자가 line에 포함되지 못한 경우, 한번 더 돌아야 함
            if idx == len_words - 1:
                is_break = True
                if is_again:
                    is_break = False


            ## 문장처리 파트
            len_line = len(line) # 단어 개수

            # total space = maxWidth - 실제 단어들의 길이 
            # (실제 단어 길이: length에는 단어 사이 공백 1개가 있다고 가정하여 계산된 것이므로, 이를 빼줌)
            total_space = maxWidth - ( length - ( len_line - 1 ) )

            # 마지막 문장인 경우, 왼쪽 정렬 처리
            if is_break:
                # 단어 사이마다 공백 하나씩 넣고 나서 남은 공백 길이는 오른쪽에 배분
                space_len_right = total_space - (len_line-1) 
                lines.append(" ".join(list(map(str, line))) + " " * space_len_right)
                break
            # 마지막 문장이 아닌 경우, 평평 처리
            else:
                # 한글자인 경우
                if len_line == 1:
                    line_str = line[0] + (" " * total_space)
                    lines.append(line_str)
                # 여러글자인 경우
                else:
                    space_num = len_line - 1 # 공백의 개수
                    space_len = total_space // space_num # 기본 공백 길이 = 가능한 공백 전체 길이 / 공백 개수 의 몫
                    space_left = total_space % space_num # 남는 공백 길이 = 위 연산의 나머지
                    # 남는 공백 개수를 하나씩 뿌리면 됨
                    space_lens = [space_len + 1 if i < space_left else space_len for i in range(space_num)]

                    new_line = []
                    for i, space_len in enumerate(space_lens):
                        new_line.append(line[i]) # 단어 하나
                        new_line.append(" " * space_len) # 지정된 공백 하나
                    new_line.append(line[i+1]) # 마지막 단어 하나

                    lines.append("".join(list(map(str, new_line))))

        return lines