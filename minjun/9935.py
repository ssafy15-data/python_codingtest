sentence = list(input()) #전체 문장
explode = input() # 폭발 문자열
len_exp = len(explode) # 폭발 문자열 길이

order = 0 # 현재 폭발 문자열 매치 인덱스
temp = [] # 임시 폭발 후보
deleted = [] # 실제 폭발한 인덱스들

for idx, char in enumerate(sentence):

    # 문자가 해당 순서의 폭발 문자와 일치한다면
    if char == explode[order]:
        temp.append((idx, order)) # 폭발 후보에 저장
        order += 1 # 순서 조정

        # 만약 마지막 폭발 문자였다면, 임시->실제 폭발
        if order == len_exp:

            # temp를 deleted로 이동해주는 과정
            while True:
                temp_idx, temp_order = temp.pop()
                deleted.append(temp_idx)
                if temp_order == 0:
                    break

            # 순서 초기화
            order = 0

            # 만약 temp에 폭발 후보가 남아있다면, 순서 재조정
            if temp:
                order = temp[-1][1] + 1

    # 문자가 폭발 문자와 일치하지 않는다면
    else:
        # 첫 폭발문자와 같다면, 처리
        if char == explode[0]:
            temp.append((idx, 0))
            order = 1
        # 그것도 아니라면, temp 초기화 (이전에 쌓여있던 것들 전부 제거)
        else:
            temp = []
            order = 0

# 실제 폭발 대상이 있다면
if deleted:            
    result = []

    # 인덱스들이므로, 정렬
    deleted.sort(reverse=True)
    delete_idx = deleted.pop()

    # 문자을 순회하며, 폭발 대상인지 확인 후, 폭발 대상이 아니라면 result에 저장
    for idx, char in enumerate(sentence):
        if idx != delete_idx:
            result.append(char)
        else:
            try:
                delete_idx = deleted.pop()
            except:
                pass

# 폭발 대상이 없다면 result = 원본 문장
else:
    result = sentence

if result:
    print(*result, sep="")
# 전부 폭파되었다면
else:
    print("FRULA")