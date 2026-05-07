class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_len = len(words)

        # 단어 저장용 temp
        current_word = []
        current_word_count = 0
        current_len = 0

        # 정답
        answer = []

        for idx in range(words_len):
            word = words[idx]
            word_len = len(word)

            # 마지막 단어의 경우
            if idx == words_len:
                pass

            print("---")
            print(word)
            print(current_len + current_word_count)
            print(current_len + current_word_count + word_len)            
            # 현재 단어를 더해도 되는 경우
            if current_len + current_word_count + word_len <= maxWidth:
                current_word.append(word)
                current_len += word_len
                current_word_count += 1
                print(current_word)
            else: # 현재 단어를 더하면 max_width를 넘는 경우
                #길이가 max_width 가 되지 않는다면
                if current_len + max(0, current_word_count - 1) != maxWidth:
                    left = maxWidth - (current_len + max(0, current_word_count - 1))
                    divide = left // (current_word_count - 1) # 각 글자 사이에 할당 가능한 공백
                    for i in range(len(current_word) - 1):
                        new_word = current_word[i] + " " * divide
                        current_word[i] = new_word
                    print(current_len + max(0, current_word_count - 1), left, current_word, divide)

                answer.append("".join(current_word))
                print(answer)
                print("-----")
                current_word = [word]
                current_len = word_len
            
        
        return answer
                


