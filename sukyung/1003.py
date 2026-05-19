# Check If Word Is Valid After Substitutions - Medium

class Solution:
    def isValid(self, s: str) -> bool:
        # 사칙연산 검사처럼 스택에 넣고 빼며 abc 검사

        st = []
        for t in s:
            if t == 'a':
                st.append(t)
            elif t == 'b':
                if st and st[-1] == 'a':    # 'ab' 합해서 push
                    pre = st.pop()
                    st.append(pre+t)
                else:
                    st.append(t)
            else:  # t == 'c'
                if st and st[-1] == 'ab':   # 'abc' 되면 삭제
                    st.pop()
                else:
                    st.append(t)
        
        if st:  # 아직 스택에 문자가 남아 있다면 s 문자를 만들 수 없는 경우임
            return False
        else:
            return True
        
# 21ms, 19.65MB