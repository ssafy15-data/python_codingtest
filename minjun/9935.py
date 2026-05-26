sentence = list(input())
explode = input()
len_exp = len(explode)

order = 0
temp = []
deleted = []

for idx, char in enumerate(sentence):
    if char == explode[order]:
        temp.append((idx, order))
        order += 1

        if order == len_exp:
            order = 0
            while True:
                temp_idx, temp_order = temp.pop()
                deleted.append(temp_idx)
                if temp_order == 0:
                    break

            if temp:
                order = temp[-1][1] + 1

    else:
        if char != explode[0]:
            temp = []
            order = 0
        else:
            temp.append((idx, 0))
            order = 1

if deleted:            
    result = []
    deleted.sort(reverse=True)
    delete_idx = deleted.pop()
    for idx, char in enumerate(sentence):
        if idx != delete_idx:
            result.append(char)
        else:
            try:
                delete_idx = deleted.pop()
            except:
                pass

else:
    result = sentence

if result:
    print(*result, sep="")
else:
    print("FRULA")